##
# first_program get first last value
def get_first_last(data):
    first = 1
    last = 2
    if len(data) > 2:
        first = data[0]
        last = data[len(data) - 1]
    return first, last


tab = [1, 2, 3, 4, 5, 6, 10, 55]
result = get_first_last(tab)
print(result[0])
print(result[1])


##
# optional value
def say_goodbye(message="Goodbye!"):
    print(message)


say_goodbye()
say_goodbye("Hello")


##
# variable parameters
def print_6_element(data):
    if len(data) > 6:
        data = data[0:6]
    return data


print(print_6_element("123456789"))


##
# with retun value
def get_value(n1, n2):
    return n1 + n2


result = get_value(9, 3)
print(result)
##
