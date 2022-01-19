import datetime
import os
import time
from typing import Generator, List, Protocol, Tuple


class FolderIterator(Protocol):

    start_time = 0
    first_file_available = 0
    last_file_available = 0

    def get_files(self, folder: str, no_log: bool = False) -> List[str]:
        self.start_time = time.time()
        if not no_log:
            print(f'\n[{self.name}] Starting getting files from {folder}')
        files = []
        for file in self._get_files(folder):
            if self.first_file_available == 0:
                self.first_file_available = time.time()
            files.append(file)
        self.last_file_available = time.time()

        stop_time = time.time()
        folders = set([os.path.dirname(file) for file in files])
        if not no_log:
            print(f'[{self.name}] Got {len(files)} files in {len(folders)} folders @ {datetime.timedelta(seconds=stop_time-start_time)}')
        return files

    def _get_files(self, folder: str) -> Generator:
        raise NotImplementedError()

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def times(self) -> Tuple[float, float, float]:
        return (self.start_time, self.first_file_available, self.last_file_available)
