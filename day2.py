PUZZLE_INPUT = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0]
TEST_INPUT = [1,1,1,4,99,5,6,0,99]


####### PART 1 #######

def run_intcode_computer(intcode_input = PUZZLE_INPUT.copy()):
    current_position = 0

    while ( ((current_position+1) * 4 ) < len(intcode_input) ):
        operation = intcode_input[current_position*4]
        first_input_position = intcode_input[current_position*4 + 1]
        second_input_position = intcode_input[current_position*4 + 2]
        output_position = intcode_input[current_position*4 + 3]
        if operation == 1:
            intcode_input[output_position] = intcode_input[first_input_position] + intcode_input[second_input_position]
        elif operation == 2:
            intcode_input[output_position] = intcode_input[first_input_position] * intcode_input[second_input_position]
        elif operation == 99:
            break
        current_position += 1
    return intcode_input

print(run_intcode_computer())

####### PART 2 #######

noun = 0
verb = 0
found = False
result = []

while noun < 100:
    while verb < 100:
        intcode = PUZZLE_INPUT.copy()
        intcode[1] = noun
        intcode[2] = verb
        try:
            result = run_intcode_computer(intcode_input=intcode)
        except:
            verb += 1
            continue
        if (result[0] == 19690720):
            found = True
            break
        verb += 1
    if (found == True):
        break
    verb = 0
    noun += 1
    

if (found == True):
    print(f'Noun = {noun}, Verb = {verb}')
    print(result)
else:
    print('Noun and Verb not found')

part2_answer = noun * 100 + verb
print(f'Answer: {part2_answer}')