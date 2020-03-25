# Disk Scheduling Algorithms in Python

This project deals with various disk scheduling algorithms and calculating the minimum amongst them i.e. the best algorithm for the provided set of data.

## Importing Data:

Data is imported from an Excel file.
For this ```xlrd``` module needs to be imported into the main file where the algorithms are compared.
```
import xlrd
```

### Excel File
Data is imported from
```
SeekTime.xls
```
This data is stored in a list that is passed to each algorithm as a function.

### ALgorithm Files
File for each algorithm need to be imported into ```main.py```.
```
import fcfs
import sstf
import look
import scan
```

## Algorithms

Disk Scheduling Algorithms that are implemented in the project are FCFS, SSTF, LOOK and SCAN(Elevator).
Each individual file contains the implementation of each algorithm namely```fcfs.py```,```sstf.py```,```look.py``` and ```scan.py```.

### Author
Mihir Thakur
