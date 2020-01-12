def my_gen(new_n):
    n = new_n
    print('This is printed first')
    for i in range(1, n):
        i += i
    # Generator function contains yield statements
    yield i

first_gen = my_gen(3)
second_gen = my_gen(2)
third_gen = my_gen(4)

