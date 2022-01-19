import os
import shutil
import unittest

from src.consts import SAMPLE_FOLDER
from src.files_generator import generate_folders_and_files
from src.glob_iterator import GlobFolderIterator
from src.iglob_iterator import IGlobFolderIterator
from src.os_walk_folder_iterator import OSWalkFolderIterator
from src.pathlib_folder_iterator import PathLibFolderIterator
from src.scandir_iterator import ScanDirIterator


class TestIterators(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:        
        shutil.rmtree(SAMPLE_FOLDER, ignore_errors=True)
        os.makedirs(SAMPLE_FOLDER)
        cls.count = len(generate_folders_and_files(SAMPLE_FOLDER, 5, 5, 20))
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(SAMPLE_FOLDER)
        return super().tearDownClass()

    def test_os_walk_iterator(self):
        iterator = OSWalkFolderIterator()
        files = iterator.get_files(SAMPLE_FOLDER)
        self.assertEqual(self.count, len(files))

    def test_glob_iterator(self):
        iterator = GlobFolderIterator()
        files = iterator.get_files(SAMPLE_FOLDER)
        self.assertEqual(self.count, len(files))

    def test_iglob_iterator(self):
        iterator = IGlobFolderIterator()
        files = iterator.get_files(SAMPLE_FOLDER)
        self.assertEqual(self.count, len(files))

    def test_scandir_iterator(self):
        iterator = ScanDirIterator()
        files = iterator.get_files(SAMPLE_FOLDER)
        self.assertEqual(self.count, len(files))

    def test_pathlib_iterator(self):
        iterator = PathLibFolderIterator()
        files = iterator.get_files(SAMPLE_FOLDER)
        self.assertEqual(self.count, len(files))
