def calcFCFS(arr, head):
    seek_dist, head = 0, 0
    if len(arr) == 0:
        return
    for i in range(len(arr)):
        # Keep adding distance between consecutive pins
        seek_dist += abs(arr[i]-head)
        # Update head to be set as the current pin
        head = arr[i]
        return seek_dist
