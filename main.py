import xlrd
from fcfs import calcFCFS
from scan import calcScan
from sstf import calcSSTF


def diskSchedduling():
    # Accessing the excel document
    wb = xlrd.open_workbook("SeekTime.xls")
    sheet = wb.sheet_by_index(0)

    sheet.cell_value(0, 0)
    # Convert the seek time provided in the first column of the excel file into a list of integers
    seek_time = list(map(int, sheet.col_values(0)))
    # The first element of the column is assumed to be the head
    head = seek_time[0]
    # Deleting the first head element such that now it is just a list of seek times for disk scheduling
    del seek_time[0]

    fcfs = calcFCFS(seek_time, head)
    sstf = calcSSTF(seek_time, head)
    scan = calcScan(seek_time, head)

    print("Seek Distance for Disk Scheduling Algorithms: ")
    print("FCFS: ", fcfs)
    print("SSTF: ", sstf)
    print("SCAN: ", scan)

    # result = [fcfs, sstf, scan]

    # Find the Algorithm with the least seek time
    if fcfs < sstf:
        if fcfs < scan:
            print("FCFS is best Option. Total SEEK Time: ", fcfs)
        elif scan < fcfs:
            print("SCAN is best Option. Total SEEK Time: ", scan)
    elif sstf < fcfs:
        if sstf < scan:
            print("SSTF is best Option. Total SEEK Time: ", sstf)
        elif scan < sstf:
            print("SCAN is best Option. Total SEEK Time: ", scan)


if __name__ == "__main__":
    diskSchedduling()