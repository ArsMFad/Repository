import random


def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


def rand_sort(arr):
    count = 0

    while (1):
        for i in range(0, len(arr) - 1):
            magic = random.randint(0, 1)
            if magic == 1:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            count += 1
            if is_sorted(arr):
                return arr


arr = list(map(int, input().split(" ")))


print(rand_sort(arr))
