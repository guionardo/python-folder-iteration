import platform

import psutil
from tabulate import tabulate

from src.consts import TABLEFMT


def print_hw_info():
    print(' System Information '.center(50, '='))
    uname = platform.uname()
    print(tabulate([[uname.system, uname.release, uname.version, uname.machine, uname.processor]],
                   headers=['System', 'Release',
                            'Version', 'Machine', 'Processor'],
                   tablefmt=TABLEFMT))

    print(' CPU Info '.center(50, '='))
    cpufreq = psutil.cpu_freq()
    print(
        tabulate([[psutil.cpu_count(logical=False), psutil.cpu_count(logical=True), cpufreq.max, cpufreq.min, round(cpufreq.current, 3)]],
                 headers=['Physical cores', 'Total cores', 'Max frequency',
                          'Min frequency', 'Current frequency'],
                 tablefmt=TABLEFMT))

    # CPU usage
    print(' CPU Usage Per Core '.center(50, '='))
    usage = []
    headers = []
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        usage.append(percentage)
        headers.append(i)
    usage.append(psutil.cpu_percent())
    headers.append('Total')

    print(tabulate([usage], headers=headers, tablefmt=TABLEFMT))

    # Memory Information
    print(" Memory Information ".center(50, '='))
    # get the memory details
    svmem = psutil.virtual_memory()
    print(tabulate([[get_size(svmem.total), get_size(
        svmem.available), get_size(svmem.used), f'{svmem.percent}%']], headers=['Total', 'Available', 'Used', 'Percentage'], tablefmt=TABLEFMT))
    print(" SWAP ".center(50, '='))
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(
        tabulate([[get_size(swap.total), get_size(swap.free), get_size(swap.used), f'{swap.percent}%']],
                 headers=['Total', 'Free', 'Used', 'Percentage'],
                 tablefmt=TABLEFMT))


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
