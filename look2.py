def calcMax(arr, head):
    maxm = 0
    for i in range(len(arr)):
        if head > arr[i] > maxm:
            maxm = arr[i]
        else:
            return min(arr)
    return maxm


def calcMin(arr, head):
    ans = []
    for i in range(len(arr)):
        if arr[i] > head:
            ans.append(arr[i])
    return arr.index(min(ans))


def calcLook(arr, head):
    start = head
    direction = "LEFT"
    seek_count = 0
    arr = sorted(arr)
    if direction == "LEFT":
        while head != min(arr):
            maxm = calcMax(arr, head)
            # print(maxm)
            seek_count += abs(maxm - head)
            # print(seek_count)
            head = maxm
    if head == min(arr):
        seek_count += start
        head = start
        head1 = calcMin(arr, start)
        for i in range(head1, len(arr)):
            seek_count += abs(arr[i] - head)
            head = arr[i]
    return seek_count


array = [60, 79, 92, 114, 176, 41, 34, 11]
print(calcLook(array, 50))
