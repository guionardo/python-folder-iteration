import os
from typing import Generator

from src.abstract_folder_iterator import FolderIterator


class ScanDirIterator(FolderIterator):

    def _get_files(self, folder: str) -> Generator:
        with os.scandir(folder) as scan:
            for item in scan:
                if item.is_file():
                    yield item.path
                else:
                    for subitem in self._get_files(item.path):
                        yield subitem
