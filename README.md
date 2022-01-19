# python-folder-iteration
Folder and files iteration comparative


## System Information

| System | Release           | Version                                            | Machine | Processor |
| ------ | ----------------- | -------------------------------------------------- | ------- | --------- |
| Linux  | 5.11.0-46-generic | #51~20.04.1-Ubuntu SMP Fri Jan 7 06:51:40 UTC 2022 | x86_64  | x86_64    |

## CPU Info

| Physical cores | Total cores | Max frequency | Min frequency | Current frequency |
| -------------- | ----------- | ------------- | ------------- | ----------------- |
| 4              | 8           | 3400          | 400           | 1.892             |

## CPU Usage Per Core

| 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | Total |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----- |
| 15.6 | 16.5 | 10.4 | 14.1 | 15.2 | 14.4 | 15.2 | 12.4 | 14    |

## Memory Information

| Total   | Available | Used   | Percentage |
| ------- | --------- | ------ | ---------- |
| 15.51GB | 4.77GB    | 9.56GB | 69.2%      |

## SWAP

| Total   | Free   | Used    | Percentage |
| ------- | ------ | ------- | ---------- |
| 15.26GB | 3.28GB | 11.98GB | 78.5%      |

```
  Creating sample files
  + Creating folder ./test_files
  + Creating files LEVELS=6 FOLDER_COUNT=6 FILE_COUNT_BY_FOLDER=20
  + Created 933120 files in  0:02:08.928680

* Running iterators: GlobFolderIterator IGlobFolderIterator OSWalkFolderIterator ScanDirIterator PathLibFolderIterator
```

## MEMORY USAGE

| Iterator              | RSS       | VMS       | DATA      |
| --------------------- | --------- | --------- | --------- |
| IGlobFolderIterator   | 111280128 | 96468992  | 96468992  |
| OSWalkFolderIterator  | 111280128 | 96468992  | 96468992  |
| ScanDirIterator       | 111280128 | 96468992  | 96468992  |
| GlobFolderIterator    | 117309440 | 102498304 | 120254464 |
| PathLibFolderIterator | 469721088 | 455081984 | 455081984 |

## ELAPSED TIME

| Iterator              | Elapsed time   | X    |
| --------------------- | -------------- | ---- |
| ScanDirIterator       | 0:00:01.317526 | 1    |
| OSWalkFolderIterator  | 0:00:02.496639 | 1.9  |
| PathLibFolderIterator | 0:00:10.464794 | 7.9  |
| IGlobFolderIterator   | 0:00:14.358165 | 10.9 |
| GlobFolderIterator    | 0:00:15.308936 | 11.6 |

## TIME FOR FIRST FILE

| Iterator              | Elapsed time   | X       |
| --------------------- | -------------- | ------- |
| ScanDirIterator       | 0:00:00.000098 | 1       |
| OSWalkFolderIterator  | 0:00:00.000247 | 2.5     |
| PathLibFolderIterator | 0:00:00.000690 | 7       |
| IGlobFolderIterator   | 0:00:00.001135 | 11.6    |
| GlobFolderIterator    | 0:00:07.831005 | 79908.2 |
  
```
Removed  ./test_files in 0:00:14.406029
```
