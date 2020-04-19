def fizz_buzz(start, stop):
    result = ''

    for x in range(start, stop + 1):
        part_fizz = 'Fizz' if x % 3 == 0 else ''
        part_buzz = 'Buzz' if x % 5 == 0 else ''
        if part_fizz or part_buzz:
            result += '{}{}' .format(part_fizz, part_buzz)
        else:
            result += str(x)
        if x != stop:
            result += ' '

    return result
print(fizz_buzz(1, 100))
