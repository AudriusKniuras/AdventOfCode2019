import itertools
# a = list(itertools.permutations([1,2,3]))
# print(a)
POSITION = 0
IMMEDIATE = 1

ADD = 1
MUL = 2
HALT = 99

Operations = {
    ADD: ()
}

class Computer:
    def __init__(self, code):


