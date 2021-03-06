# Create a sequence according to the Scan Algorithms and then return it
# to simply calculate the difference and get total seek time
# Direction of pin assumed to be to the left.


def arrangeArray(arr, head):
    # 'lower' for elements less than 'head'
    # 'higher' for elements greater than 'head
    lower, higher = [], []
    for i in arr:
        if i < head:
            lower.append(i)
        if i > head:
            higher.append(i)
    lower.append(0)
    lower = sorted(lower, reverse=True)             # Descending order
    higher = sorted(higher)                         # Ascending order
    # Merge both to get the final sequence.
    seq = lower + higher
    return seq


def calcSCAN(arr, head):
    seek_time = 0
    if len(arr) == 0:
        return
    for i in range(len(arr)):
        # Keep adding distance between consecutive pins
        seek_time += abs(arr[i] - head)
        # Update head to be set as the current pin
        head = arr[i]
        return seek_time

#print(arrangeArray([12,45,67,98,22,177,84,36], 50))
