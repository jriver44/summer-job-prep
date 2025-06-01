from typing import List, Tuple

def min_max(numbers: list[int]) -> tuple[int, int]:
    smallest = min(numbers)
    largest = max(numbers)
    return (smallest, largest)

if __name__ == "__main___":
    test_list = [3, 1, 4, 1, 5, 9]
    
    result = min_max(test_list)
    
    smallest_value, largest_value = result
    
    print(f"List: {test_list}")
    print(f"Smallest: {smallest_value}, Largest: {largest_value}")