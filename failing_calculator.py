def average_ratios(numbers):
    total = 0
    valid_count = 0

    for number in numbers:
        if number == 0:
            continue
        total += 100 / number
        valid_count += 1

    if valid_count == 0:
        raise ValueError("At least one non-zero number is required")

    return total / valid_count

print(average_ratios([10, 5, 0]))
