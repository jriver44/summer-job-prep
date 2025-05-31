from typing import List

def parse_input_to_int_list(line: str) -> List[int]:
    
    string_parts: List[str] = line.split()
    
    int_list: List[int] = [int(part) for part in string_parts]
    
    return int_list

def unique_sorted(numbers: List[int]) -> List[int]:
    unique_set = set(numbers)
    
    unique_list = list(unique_set)
    
    unique_list.sort()
    
    return unique_list

if __name__ == "__main__":
    raw_input: str = input("Enter integers separated by spaces:\n")
    
    nums: List[int] = parse_input_to_int_list(raw_input)
    
    result: List[int] = unique_sorted(nums)
    
    print("\nUnique, sorted list:")
    print(result)