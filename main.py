import datetime
import os
import shutil
from time import time
from typing import List

import psutil
import tabulate

from src.abstract_folder_iterator import FolderIterator
from src.consts import SAMPLE_FOLDER,TABLEFMT
from src.files_generator import generate_folders_and_files
from src.glob_iterator import GlobFolderIterator
from src.hw_info import print_hw_info
from src.iglob_iterator import IGlobFolderIterator
from src.os_walk_folder_iterator import OSWalkFolderIterator
from src.pathlib_folder_iterator import PathLibFolderIterator
from src.scandir_iterator import ScanDirIterator

iterators: List[FolderIterator] = [iterator() for iterator in [GlobFolderIterator,
                                                               IGlobFolderIterator,
                                                               OSWalkFolderIterator,
                                                               ScanDirIterator,
                                                               PathLibFolderIterator]]

LEVELS = 6
FOLDER_COUNT = 6
FILE_COUNT_BY_FOLDER = 20
FILES_COUNT = 0
PROCESS = None


def _create_sample_folder():
    print('  Creating sample files')
    print('  + Creating folder', SAMPLE_FOLDER)
    shutil.rmtree(SAMPLE_FOLDER, ignore_errors=True)
    os.makedirs(SAMPLE_FOLDER)
    print(
        f'  + Creating files LEVELS={LEVELS} FOLDER_COUNT={FOLDER_COUNT} FILE_COUNT_BY_FOLDER={FILE_COUNT_BY_FOLDER}')
    start_time = time()
    files = generate_folders_and_files(
        SAMPLE_FOLDER, LEVELS, FOLDER_COUNT, FILE_COUNT_BY_FOLDER)
    globals()['FILES_COUNT'] = len(files)
    print(f'  + Created {len(files)} files in ',
          datetime.timedelta(seconds=time()-start_time))


def _memory(start: bool) -> dict:
    m = PROCESS.memory_info()
    result = dict(rss=m.rss,
                  vms=m.vms,
                  data=m.data)

    if start:
        globals()['MEMORY'] = result
    else:
        m = globals()['MEMORY']
        result['rss_delta'] = result['rss']-m['rss']
        result['vms_delta'] = result['vms']-m['vms']
        result['data_delta'] = result['data']-m['data']

    return result


def main():
    globals()['PROCESS'] = psutil.Process()
    print('* Folder iteration strategies benchmark\n')
    print_hw_info()
    table = []
    try:
        _create_sample_folder()
        print('\n* Running iterators: ', end='')
        for iterator in iterators:
            print(f'{iterator.name} ', end='')
            _memory(True)
            files = iterator.get_files(SAMPLE_FOLDER, True)
            start_time, first_file_available, last_file_available = iterator.times
            memory_result = _memory(False)
            elapsed_time = datetime.timedelta(
                seconds=last_file_available-start_time)
            if len(files) != FILES_COUNT:
                print(
                    f' Fail to get files. Expected={FILES_COUNT} Got={len(files)}')
                return
            del(files)
            table.append([
                iterator.name, elapsed_time,
                0,
                datetime.timedelta(seconds=first_file_available-start_time),
                memory_result['rss_delta'],
                memory_result['vms_delta'],
                memory_result['data_delta']])
        print()
        print(' MEMORY USAGE '.center(40, '#'))
        table_memory = [[r[0], r[4], r[5], r[6]]
                        for r in sorted(table, key=lambda row:row[4])]
        print(tabulate.tabulate(table_memory,
                                headers=['Iterator', 'RSS', 'VMS', 'DATA'],
                                tablefmt=TABLEFMT))

        _print_table('ELAPSED TIME', table, 1, 'Elapsed time')
        _print_table('TIME FOR FIRST FILE', table, 3, 'Elapsed time')

    finally:
        start_time = time()
        shutil.rmtree(SAMPLE_FOLDER, ignore_errors=True)
        print('  Removed ', SAMPLE_FOLDER, 'in',
              datetime.timedelta(seconds=time()-start_time))
        print('* Finished')


def _print_table(title: str, table: list, col_index: int, col_name: str):
    print('\n', f' {title.strip()} '.center(40, '#'))
    sorted_table = sorted(table, key=lambda row: row[col_index])
    first_data = sorted_table[0][col_index].total_seconds()
    new_table = [[row[0],
                  row[col_index],
                  round(row[col_index].total_seconds()/first_data, 1)
                  ]
                 for row in sorted_table]

    print(tabulate.tabulate(new_table,
                            headers=['Iterator', col_name, 'X'],
                            tablefmt=TABLEFMT))


if __name__ == '__main__':
    main()
