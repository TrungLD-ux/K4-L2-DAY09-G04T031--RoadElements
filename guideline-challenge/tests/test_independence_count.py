import json
from pathlib import Path
import tempfile
import unittest

from lab9 import LabError
from lab9.scoring import _independence_count


class IndependenceEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.path = self.base / 'project/07_blind_handoff/clarification_count.json'
        self.path.parent.mkdir(parents=True)

    def evidence(self, low, high, source='group-reported range'):
        self.path.write_text(json.dumps(dict(minimum=low, maximum=high, source=source)), encoding='utf-8')

    def test_legacy_bands_are_unchanged(self):
        for count, expected in [(0, 100), (1, 70), (2, 70), (3, 40), (4, 40), (5, 0), (20, 0)]:
            with self.subTest(count=count):
                score, low, high, display, note = _independence_count(self.base, count)
                self.assertEqual((score, low, high, display, note), (expected, count, count, str(count), ''))

    def test_reported_range_does_not_become_zero_questions(self):
        self.evidence(5, 20)
        score, low, high, display, note = _independence_count(self.base, 0)
        self.assertEqual((score, low, high, display), (0, 5, 20, '5–20'))
        self.assertIn('group-reported range', note)
        self.assertIn('0', note)

    def test_range_crossing_rubric_bands_is_rejected(self):
        for low, high in [(0, 1), (2, 3), (4, 5)]:
            self.evidence(low, high)
            with self.assertRaises(LabError):
                _independence_count(self.base, 0)

    def test_invalid_or_unsourced_ranges_are_rejected(self):
        for low, high, source in [(-1, 5, 'x'), (20, 5, 'x'), (True, 5, 'x'), (5, 20.5, 'x'), (5, 20, '')]:
            self.evidence(low, high, source)
            with self.assertRaises(LabError):
                _independence_count(self.base, 0)

    def test_recorded_questions_cannot_exceed_reported_maximum(self):
        self.evidence(5, 20)
        with self.assertRaises(LabError):
            _independence_count(self.base, 21)


if __name__ == '__main__':
    unittest.main()
