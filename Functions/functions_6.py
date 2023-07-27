def running_sums(numbers):
    sums = []

    current_sum = 0
    for number in numbers:
        current_sum += number
        sums.append(current_sum)

    return sums

print(running_sums([5, 4, 10, 20 ,25]))