def filter_lines_by_keyword(input_path: str, output_path: str, keyword:str) -> None:
    lowered_keyword = keyword.lower()
    
    with open(input_path, 'r') as infile:
        with open(output_path, 'w') as outfile:
            for line in infile:
                if lowered_keyword in line.lower():
                    outfile.write(line)

if __name__ == "__main__":
    keyword = input("Enter keyword to be filtered (case-insensitive): ").strip()
    
    input_file_path = "test_files/input.txt"
    output_file_path = "test_files/output.txt"
    
    filter_lines_by_keyword(input_file_path, output_file_path, keyword)
    
    print(f"Lines containing '{keyword}' have been written to '{output_file_path}'.")