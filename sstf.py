def calcMin(arr, head, diff):
    minm = 99999999
    for i in range(len(arr)):
        diff[i][0] = abs(arr[i]-head)
    for i in range(len(arr)):
        if not diff[i][1] and minm > diff[i][0]:
            minm = diff[i][0]
            index = i
    return index


def calcSSTF(arr, head):
    diff = []
    seek_seq = [0]*(len(arr)+1)
    seek_count = 0
    for i in range(len(arr)):
        diff.insert(i, [0, 0])

    for i in range(len(arr)):
        seek_seq[i] = head
        index = calcMin(arr, head, diff)

        diff[index][1] = True
        seek_count += diff[index][0]

        head = arr[index]

    return seek_count
