import os
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

FOLDER_NAMES = ['alpha', 'beta', 'gamma', 'delta', 'epsilon',
                'zeta', 'eta', 'theta', 'iota', 'kappa']

sample = {
    'alpha': {'alpha': {'alpha': None, 'beta': None, 'gamma': None},
              'beta': {'alpha': None, 'beta': None, 'gamma': None},
              'gamma': {'alpha': None, 'beta': None, 'gamma': None}},
    'beta': {'alpha': {'alpha': None, 'beta': None, 'gamma': None},
             'beta': {'alpha': None, 'beta': None, 'gamma': None},
             'gamma': {'alpha': None, 'beta': None, 'gamma': None}},
    'gamma': {'alpha': {'alpha': None, 'beta': None, 'gamma': None},
              'beta': {'alpha': None, 'beta': None, 'gamma': None},
              'gamma': {'alpha': None, 'beta': None, 'gamma': None}}
}


def generate_folders_list(base_path: str, levels: int, folder_count: int) -> list:
    if not os.path.isdir(base_path):
        raise FileNotFoundError(base_path)
    _validate_number(levels, 1, 10, 'levels')
    _validate_number(folder_count, 1, 10, 'folder_count')

    folders_dict = {}
    _generate_folder(folders_dict, 1, levels, folder_count)
    return list(_generate_folder_list(base_path, folders_dict))


def generate_files_list(folder_list: List[str], file_count_by_folder: int) -> List[str]:
    _validate_number(file_count_by_folder, 0, 100_000, 'file_count_by_folder')
    files_list = []
    for folder in folder_list:
        for file_id in range(file_count_by_folder):
            files_list.append(os.path.join(folder, f'file_{file_id:06}'))

    return files_list


def create_file(filename: str):

    try:
        with open(filename, 'w') as file:
            file.write('')
        return (filename, None)

    except Exception as exc:
        return (filename, exc)


def generate_folders_and_files(base_path: str, levels: int, folder_count: int, file_count_by_folder: int) -> List[Tuple[str, Exception]]:
    folders = generate_folders_list(base_path, levels, folder_count)
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    files = generate_files_list(folders, file_count_by_folder)
    with ThreadPoolExecutor(4, 'file_generator') as executor:
        result = executor.map(create_file, files)

    return list([result][0])


def _generate_folder(fdict: dict, level: int, max_level: int, folder_count: int):
    if level > max_level:
        return
    for folder in FOLDER_NAMES[0:folder_count]:
        fdict[folder] = {}
        _generate_folder(fdict[folder], level+1, max_level, folder_count)


def _generate_folder_list(base_path: str, folders_dict: dict):
    for key in folders_dict:
        if not folders_dict[key]:
            yield os.path.join(base_path, key)
        else:
            for folder in _generate_folder_list(os.path.join(base_path, key), folders_dict[key]):
                yield folder


def _validate_number(value: int, min_value: int, max_value: int, value_name: str):
    if min_value <= value <= max_value:
        return
    raise ValueError(
        f'{value_name} must be between {min_value} and {max_value}', value)
