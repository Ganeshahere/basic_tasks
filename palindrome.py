import prompt
def is_palindrome(string):
    pointer1 = 0
    pointer2 = len(string) - 1
    while pointer2 - pointer1 > 0:
        if string[pointer1] != string[pointer2]:
            print('False')
            return False
        pointer1 += 1
        pointer2 -= 1
    print('True')
    return True
string = prompt.string('Inpit your string: ')
is_palindrome(string)
