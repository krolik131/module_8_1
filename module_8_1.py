def add_everything_up(a,b):
    try:
        add = a+b
        return add

    except TypeError as e:
        print(e)

        return f'{a,b}'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))