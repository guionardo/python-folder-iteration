import os
from typing import Generator

from src.abstract_folder_iterator import FolderIterator


class OSWalkFolderIterator(FolderIterator):

    def _get_files(self, folder: str) -> Generator:
        for root, _, files in os.walk(folder):
            for file in files:
                yield os.path.join(root, file)
