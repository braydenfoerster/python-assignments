def without_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example
if __name__ == "__main__":
    my_list = [10, 'hi', 10, True, -50000.7, 'hi', 10]
    result = without_duplicates(my_list)
    print(result)
