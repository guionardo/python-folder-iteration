import pathlib
from typing import Generator

from src.abstract_folder_iterator import FolderIterator


class PathLibFolderIterator(FolderIterator):

    def _get_files(self, folder: str) -> Generator:
        for path in pathlib.Path(folder).rglob('*'):
            if path.is_file():
                yield str(path)
