import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def main():
    # Example usage
    data = [random.randint(1, 100) for _ in range(10)]
    print("Before sorting:", data)
    sorted_data = quick_sort(data)
    print("After sorting:", sorted_data)

if __name__ == "__main__":
    main()
