import csv

def print_rows_from_file(input_file: str) -> None:
    total = 0
    count = 0
    
    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            print(row)
            
            try:
                num = int(row[0])
                total += num
                count += 1
            except (ValueError, IndexError):
                continue
            
    if count > 0: 
        average = total / count
        print(f"\nAverage of column 1: {average}")
    else:
        print("\nNo valid numberic data found in column 1.")

if __name__ == "__main__":
    
    input_file = "test_files/data.csv"
    
    print_rows_from_file(input_file)