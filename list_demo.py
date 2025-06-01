user_input = input("Enter a list of strings seperated by commas: ")
string_list = [s.strip() for s in user_input.split(',')]
print("You Entered: ", string_list)

sorted_list = sorted(string_list)
print("Sorted List: ", sorted_list)

sorted_list.reverse()
print("Reverse Sorted List: ", sorted_list)

sorted_list.reverse()
doubled = [sorted_list * 2 for sorted_list in sorted_list]
print("Doubled List: ", doubled)