import glob
import os
from typing import Generator

from src.abstract_folder_iterator import FolderIterator


class GlobFolderIterator(FolderIterator):

    def _get_files(self, folder: str) -> Generator:
        for file in glob.glob(os.path.join(folder, '**', '*'), recursive=True):
            if os.path.isfile(file):
                yield file
