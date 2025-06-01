from filter_lines import filter_lines_by_keyword

import os

HERE = os.path.dirname(__file__)
KEYWORD = "warning"
INPUT_PATH = os.path.join(HERE, "../test_files/input.txt")
OUTPUT_PATH = os.path.join(HERE, "../test_files/output.txt")

filter_lines_by_keyword(INPUT_PATH, OUTPUT_PATH, KEYWORD)

print(f"Filtered lines containing '{KEYWORD}' writtern to '{OUTPUT_PATH}'.")