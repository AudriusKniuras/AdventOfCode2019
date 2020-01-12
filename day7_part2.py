from itertools import permutations

PUZZLE_INPUT = [3,8,1001,8,10,8,105,1,0,0,21,38,47,72,97,122,203,284,365,446,99999,3,9,1001,9,3,9,1002,9,5,9,1001,9,4,9,4,9,99,3,9,102,3,9,9,4,9,99,3,9,1001,9,2,9,102,5,9,9,101,3,9,9,1002,9,5,9,101,4,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,101,2,9,9,102,3,9,9,1001,9,2,9,4,9,99,3,9,101,3,9,9,102,2,9,9,1001,9,4,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99]
TEST_INPUT = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]


####### PART 1 #######

INPUT_VALUE = 5

# PUZZLE_INPUT = TEST_INPUT

def parameter_mode(intcode, mode, parameter):
    if mode == '0':
        return intcode[parameter]
    elif mode == '1':
        return parameter

def addition(intcode, instruction, curr_pos):
    for i in range(len(instruction), 4):
        instruction.insert(0, '0')
    
    first_parameter = parameter_mode(intcode, instruction[1], intcode[curr_pos+1])
    second_parameter = parameter_mode(intcode, instruction[0], intcode[curr_pos+2])

    output = first_parameter + second_parameter
    return output

def multiply(intcode, instruction, curr_pos):
    for i in range(len(instruction), 4):
        instruction.insert(0, '0')

    first_parameter = parameter_mode(intcode, instruction[1], intcode[curr_pos+1])
    second_parameter = parameter_mode(intcode, instruction[0], intcode[curr_pos+2])
    output = first_parameter * second_parameter
    return output

# TODO: JUMP TESTS FAIL:
def jump_if_true(intcode, instruction, curr_pos):
    for i in range(len(instruction), 4):
        instruction.insert(0, '0')

    first_parameter = parameter_mode(intcode, instruction[1], intcode[curr_pos+1])
    second_parameter = parameter_mode(intcode, instruction[0], intcode[curr_pos+2])

    if first_parameter != 0:
        curr_pos = second_parameter
    else:
        curr_pos += 3
    return curr_pos
# TODO: JUMP TESTS FAIL:
def jump_if_false(intcode, instruction, curr_pos):
    for i in range(len(instruction), 4):
        instruction.insert(0, '0')

    first_parameter = parameter_mode(intcode, instruction[1], intcode[curr_pos+1])
    second_parameter = parameter_mode(intcode, instruction[0], intcode[curr_pos+2])

    if first_parameter == 0:
        curr_pos = second_parameter
    else:
        curr_pos += 3
    return curr_pos

def less_than(intcode, instruction, curr_pos):
    for i in range(len(instruction), 4):
        instruction.insert(0, '0')

    first_parameter = parameter_mode(intcode, instruction[1], intcode[curr_pos+1])
    second_parameter = parameter_mode(intcode, instruction[0], intcode[curr_pos+2])

    if first_parameter < second_parameter:
        return 1
    else:
        return 0

def equal_parameters(intcode, instruction, curr_pos):
    for i in range(len(instruction), 4):
        instruction.insert(0, '0')

    first_parameter = parameter_mode(intcode, instruction[1], intcode[curr_pos+1])
    second_parameter = parameter_mode(intcode, instruction[0], intcode[curr_pos+2])

    if first_parameter == second_parameter:
        return 1
    else:
        return 0



def run_intcode_computer(intcode_input = PUZZLE_INPUT.copy(), phase_setting = 0, amplified_signal = INPUT_VALUE,
                        curr_pos = 0, input_count = 1):
    current_position = curr_pos
    input_count = input_count
    opcode = 0

    while current_position < len(intcode_input):
        operation = intcode_input[current_position]
        # print(operation)
        if operation%100 == 1:
            output = addition(intcode_input, list(str(operation)), current_position)
            output_position = intcode_input[current_position+3]
            
            intcode_input[output_position] = output
            current_position += 4
        elif operation%100 == 2:
            output = multiply(intcode_input, list(str(operation)), current_position)
            output_position = intcode_input[current_position+3]

            intcode_input[output_position] = output
            current_position += 4

        elif operation == 3:
            output_position = intcode_input[current_position+1]
            if input_count == 1:
                intcode_input[output_position] = phase_setting
                input_count += 1
            elif input_count > 1:
                intcode_input[output_position] = amplified_signal

            current_position += 2

        elif operation == 4:
            output_position = intcode_input[current_position+1]

            #print(f'OPCODE4: {intcode_input[output_position]}')
            opcode = intcode_input[output_position]
            current_position += 2
            return [opcode, current_position, input_count, intcode_input]

        elif operation%100 == 5:
            current_position = jump_if_true(intcode_input, list(str(operation)), current_position)

        elif operation%100 == 6:
            current_position = jump_if_false(intcode_input, list(str(operation)), current_position)

        elif operation%100 == 7:
            output_position = intcode_input[current_position+3]
            output = less_than(intcode_input, list(str(operation)), current_position)
            
            intcode_input[output_position] = output
            current_position += 4
        elif operation%100 == 8:
            output_position = intcode_input[current_position+3]
            output = equal_parameters(intcode_input, list(str(operation)), current_position)

            intcode_input[output_position] = output
            current_position += 4
        elif operation%100 == 99:
            print("BREAK reached")
            break
        else:
            print("LOOP")
            break
    # return opcode
    # return "RETURN REACHED"

#print(run_intcode_computer())




def phase_booster(phase_setting, amplified_signal):
    for phase in phase_setting:
        amplified_signal = run_intcode_computer(phase_setting = phase, amplified_signal = amplified_signal)
    return amplified_signal

def signal_amplifier():
    biggest_signal = 0
    perm_phase_array = list(permutations([0,1,2,3,4]))

    for perm in perm_phase_array:
        signal = phase_booster(phase_setting = perm, amplified_signal = 0)
        if signal > biggest_signal:
            biggest_signal = signal

    return biggest_signal

# signal = signal_amplifier()
# print(f'Day7, part1: {signal}')

def signal_amplifier_feedback_loop():
    biggest_signal = 0
    perm_phase_array = list(permutations([5,6,7,8,9]))
    # perm = [9,8,7,6,5]
    for perm in perm_phase_array:
        e = [0,0,1,PUZZLE_INPUT.copy()]
        a = [0,0,1,PUZZLE_INPUT.copy()]
        b = [0,0,1,PUZZLE_INPUT.copy()]
        c = [0,0,1,PUZZLE_INPUT.copy()]
        d = [0,0,1,PUZZLE_INPUT.copy()]
        while e != "BREAK reached":
            a = run_intcode_computer(intcode_input=a[3],phase_setting=perm[0], amplified_signal=e[0], curr_pos=a[1], input_count=a[2])
            # print(f'A: {a[0]}')
            if isinstance(a, list):
                b = run_intcode_computer(intcode_input=b[3],phase_setting=perm[1], amplified_signal=a[0], curr_pos=b[1], input_count=b[2])
            else:
                break
            # print(f'B: {b}')
            c = run_intcode_computer(intcode_input=c[3],phase_setting=perm[2], amplified_signal=b[0], curr_pos=c[1], input_count=c[2])
            # print(f'C: {c}')
            d = run_intcode_computer(intcode_input=d[3],phase_setting=perm[3], amplified_signal=c[0], curr_pos=d[1], input_count=d[2])
            # print(f'D: {d}')
            e = run_intcode_computer(intcode_input=e[3],phase_setting=perm[4], amplified_signal=d[0], curr_pos=e[1], input_count=e[2])
            if e[0] > biggest_signal:
                print(f'Biggest signal found: {e[0]}')
                biggest_signal = e[0]

signal_amplifier_feedback_loop()