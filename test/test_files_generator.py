import os
import pprint
import shutil
import unittest
from src.consts import SAMPLE_FOLDER


from src.files_generator import (generate_files_list,
                                 generate_folders_and_files,
                                 generate_folders_list)


class TestFilesGenerator(unittest.TestCase):

    def test_generate_folders_list(self):
        folders = generate_folders_list('.', 2, 2)
        self.assertEqual(4, len(folders))
        pprint.pprint(folders)

    def test_generate_files_list(self):
        folders = generate_folders_list('.', 2, 2)
        files = generate_files_list(folders, 10)
        self.assertEqual(40, len(files))

    def test_generate_folder_and_files(self):

        shutil.rmtree(SAMPLE_FOLDER, ignore_errors=True)
        os.makedirs(SAMPLE_FOLDER, exist_ok=True)
        result = generate_folders_and_files(SAMPLE_FOLDER, 3, 4, 10)
        self.assertEqual(640, len(result))
        shutil.rmtree(SAMPLE_FOLDER, ignore_errors=True)
