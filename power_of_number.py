import prompt

def is_power_of_three():
    number = prompt.integer('Input number to define')
    power_req = prompt.integer('Input required power')
    counter = 1
    while counter < number:
        counter *= power_req
    if counter == number:
        print('Number is power')
    else:
        print('Number is not power')
is_power_of_three()
