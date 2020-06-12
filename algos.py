import time


def bubble_sort(data, draw_data, time_tick):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['red' if x == j or x == j + 1 else 'cyan' for x in range(len(data))])
                time.sleep(time_tick)


def quick_sort(data, start, end, draw_data, time_tick):
    if start >= end:
        return
    pivot = data[end]
    border = start

    draw_data(data, get_colour_array(len(data), start, end, border, border))
    time.sleep(time_tick)

    for i in range(start, end):
        if data[i] < pivot:
            draw_data(data, get_colour_array(len(data), start, end, border, i))
            time.sleep(time_tick)
            data[i], data[border] = data[border], data[i]
            border += 1
        draw_data(data, get_colour_array(len(data), start, end, border, i))
        time.sleep(time_tick)
    data[end], data[border] = data[border], data[end]
    quick_sort(data, start, border - 1, draw_data, time_tick)
    quick_sort(data, border + 1, end, draw_data, time_tick)


def get_colour_array(data_len, start, end, border, current):
    colour_array = []
    for i in range(data_len):
        if start <= i <= end:
            colour_array.append('cyan')
        else:
            colour_array.append('gray40')

        if i == end:
            colour_array[i] = 'green3'
        elif i == border:
            colour_array[i] = 'yellow2'
        elif i == current:
            colour_array[i] = 'red'
    return colour_array


def merge_sort(data, l, r, draw_data, time_tick):
    if l < r:
        mid = (l + r) // 2
        merge_sort(data, l, mid, draw_data, time_tick)
        merge_sort(data, mid + 1, r, draw_data, time_tick)
        merge(data, l, mid, r, draw_data, time_tick)


def merge(arr, start, mid, end, draw_data, time_tick):
    start2 = mid + 1

    if arr[mid] <= arr[start2]:
        return

    while start <= mid and start2 <= end:
        draw_data(arr, ['red' if x == start or x == start2 + 1 else 'cyan' for x in range(len(arr))])
        time.sleep(time_tick)
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            start += 1
            mid += 1
            start2 += 1


def heapsort(arr, draw_data, time_tick):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, draw_data, time_tick)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, draw_data, time_tick)


def heapify(arr, n, i, draw_data, time_tick):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    draw_data(arr, ['red' if x == i or x == largest else 'cyan' for x in range(len(arr))])
    time.sleep(time_tick)
    if left < n and arr[left] > arr[largest]:
        largest = left
        draw_data(arr, ['red' if x == right or x == largest else 'cyan' for x in range(len(arr))])
    if right < n and arr[right] > arr[largest]:
        largest = right
        draw_data(arr, ['red' if x == left or x == largest else 'cyan' for x in range(len(arr))])
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, draw_data, time_tick)


def insertionsort(arr, draw_data, time_tick):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            draw_data(arr, ["red" if x == j or x == i else "cyan" for x in range(len(arr))])
            time.sleep(time_tick)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selectionsort(arr, draw_data, time_tick):
    for i in range(len(arr)):
        minidx = i
        for j in range(i + 1, len(arr)):
            draw_data(arr, ["red" if x == j or x == minidx else "cyan" for x in range(len(arr))])
            time.sleep(time_tick)
            if arr[j] < arr[minidx]:
                minidx = j
        arr[minidx], arr[i] = arr[i], arr[minidx]
