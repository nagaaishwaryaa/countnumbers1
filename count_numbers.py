def count_number_types(numbers):
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    return positive_count, negative_count, zero_count

# Example usage
number_list = [1, -2, 0, 3, -4, 5, 0, -6, 7, 8, -9, 0]

positives, negatives, zeros = count_number_types(number_list)

print(f"Positive numbers: {positives}")
print(f"Negative numbers: {negatives}")
print(f"Zero numbers: {zeros}")
