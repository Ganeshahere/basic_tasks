import prompt
def t(num):
    response = ('Fizz' if num % 3 == 0 else '') + ('Buzz' if num % 5 == 0 else '')
    return str(num) if not response else response

def fizz_buzz(start, stop):
    return ' '.join(map(t, range(start, stop + 1)))
start = prompt.integer('enter start: ')
stop = prompt. integer('enter stop: ')
print(fizz_buzz(start, stop))
