import unittest
from pathlib import Path

from viki.scanner import scan_video_file


class ScannerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f"{cls.__name__} start.")

    def test_no_exists(self):
        with self.assertRaises(FileNotFoundError):
            scan_video_file('none_exist_file')

    def test_file(self):
        FILE_PATH = 'examples/한글.avi'
        video = scan_video_file(FILE_PATH)
        self.assertEqual(video.id, Path(FILE_PATH))


if __name__ == '__main__':
    unittest.main()
