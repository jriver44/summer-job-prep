from typing import Dict, List, Tuple

def count_word_frequencies(text: str) -> Dict[str, int]:
    words: List[str] = text.split()
    
    freq: Dict[str, int] = {}
    
    for word in words:
        normalized: str = word.lower()
        freq[normalized] = freq.get(normalized, 0) + 1
    return freq

def sort_frequencies(freq: Dict[str, int]) -> List[Tuple[str, int]]:
    items: List[Tuple[str, int]] = list(freq.items())
    
    items.sort(key=lambda pair: (-pair[1], pair[0]))
    
    return items

if __name__ == "__main__":
    line: str = input("Enter a line of text:\n")
    
    frequencies: Dict[str, int] = count_word_frequencies(line)
    
    sorted_list: List[Tuple[str, int]] = sort_frequencies(frequencies)
    
    print("\nWord frequencies (descending order):")
    for word, count in sorted_list:
        print(f"{word}: {count}")

