from filter_lines import filter_lines_by_keyword

KEYWORD = "warning"
INPUT_PATH = "test_files/input.txt"
OUTPUT_PATH = "test_files/output.txt"

filter_lines_by_keyword(INPUT_PATH, OUTPUT_PATH, KEYWORD)

print(f"Filtered lines containing '{KEYWORD}' writtern to '{OUTPUT_PATH}'.")