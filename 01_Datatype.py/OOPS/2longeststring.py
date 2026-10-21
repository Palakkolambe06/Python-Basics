def get_max(*num):
    # If no strings are provided, return None
    if len(num) == 0:
        return None

    # Assume the first string is the longest
    max_num = num[0]

    # Check each string
    for n in num:
        # Compare the lengths of the strings
        if len(n) > len(max_num):
            max_num = n

    # Return the longest string
    return max_num


# Print the longest string
print(get_max('A', 'B', 'C', 'd', 'elephant'))
