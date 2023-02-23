import math


def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target_number:
            return mid
        elif array[mid] < target_number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def interpolation_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        t = (target - array[left]) / (array[right] - array[left])
        mid = (left + math.floor(t * (right - left)))

        if array[mid] == target_number:
            return mid
        elif array[mid] < target_number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    A = [1, 3, 4, 5, 7, 9, 11, 15, 16, 17, 19]
    target_number = 17
    binary_result = binary_search(A, target_number)
    interpolation_result = interpolation_search(A, target_number)
    print(binary_result)
    print(interpolation_result)
