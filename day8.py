from colorama import init
init(convert=True)

PUZZLE_INPUT = open('day8.in').read()

WIDTH = 25
LENGTH = 6

AREA = WIDTH * LENGTH

# class bcolors:
    # BLACK = '\u001b[40m'
    # WHITE = '\u001b[37m'
    # BLACK = '\u033[40m'
    # WHITE = '\u033[37m'

def input_to_layers(input=PUZZLE_INPUT, layer_size = AREA):
    return (input[i:i+layer_size] for i in range(0, len(input), layer_size))

def layer_fewest_zeroes(layers = input_to_layers()):
    fewest_zero_count = 100000
    fewest_zero_layer = ''
    for layer in layers:
        zero_count = list(str(layer)).count('0')
        if zero_count < fewest_zero_count:
            fewest_zero_count = zero_count
            fewest_zero_layer = layer
    return fewest_zero_layer

def part1(fewest_zero_layer = layer_fewest_zeroes()):
    ones = list(str(fewest_zero_layer)).count('1')
    twos = list(str(fewest_zero_layer)).count('2')
    return ones * twos

print(f'Part1: {part1()}')

######## PART 2 #########

def decode_image(layers = input_to_layers(), layer_size = AREA):
    decoded_image = ['2' for i in range(0, layer_size)]
    for layer in layers:
        for index,number in enumerate(layer):
            if decoded_image[index] == '2':
                decoded_image[index] = number
    return decoded_image


def display_image(input = decode_image(), width=WIDTH, length = LENGTH):
    split_image = input_to_layers(input, width)
    print(split_image)

    for line in split_image:
        chars = ""
        for char in line:
            if char == '1':
                # chars += "\u001b[47m F \u001b[0m"
                chars += '█'
            elif char == '0':
                chars += ' '
                # chars += "\u001b[40m A \u001b[0m"
        print(chars)

display_image()