PUZZLE_INPUT = [3,225,1,225,6,6,1100,1,238,225,104,0,1001,152,55,224,1001,224,-68,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,62,41,225,1101,83,71,225,102,59,147,224,101,-944,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,2,40,139,224,1001,224,-3905,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1101,6,94,224,101,-100,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1102,75,30,225,1102,70,44,224,101,-3080,224,224,4,224,1002,223,8,223,1001,224,4,224,1,223,224,223,1101,55,20,225,1102,55,16,225,1102,13,94,225,1102,16,55,225,1102,13,13,225,1,109,143,224,101,-88,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1002,136,57,224,101,-1140,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,101,76,35,224,1001,224,-138,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,374,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,389,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,404,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,419,1001,223,1,223,8,226,677,224,102,2,223,223,1005,224,434,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,449,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,479,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,494,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,524,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,539,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,554,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,569,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,584,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,599,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,614,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,629,101,1,223,223,107,226,677,224,102,2,223,223,1006,224,644,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]
TEST_INPUT = [3,9,7,9,10,9,4,9,99,-1,8]




####### PART 1 #######

INPUT_VALUE = 100
PUZZLE_INPUT = TEST_INPUT



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

def jump_if_true(intcode, instruction, curr_pos):
    for i in range(len(instruction), 4):
        instruction.insert(0, '0')

    first_parameter = parameter_mode(intcode, instruction[1], intcode[curr_pos+1])
    second_parameter = parameter_mode(intcode, instruction[0], intcode[curr_pos+2])

    if intcode[first_parameter] != 0:
        curr_pos = second_parameter
    else:
        curr_pos += 3
    return curr_pos

def jump_if_false(intcode, instruction, curr_pos):
    for i in range(len(instruction), 4):
        instruction.insert(0, '0')

    first_parameter = parameter_mode(intcode, instruction[1], intcode[curr_pos+1])
    second_parameter = parameter_mode(intcode, instruction[0], intcode[curr_pos+2])

    if intcode[first_parameter] == 0:
        curr_pos = second_parameter
    else:
        curr_pos += 3
    return curr_pos

def less_than(intcode, instruction, curr_pos):
    first_parameter = parameter_mode(intcode, instruction[1], intcode[curr_pos+1])
    second_parameter = parameter_mode(intcode, instruction[0], intcode[curr_pos+2])

    if first_parameter < second_parameter:
        return 1
    else:
        return 0

def equal_parameters(intcode, instruction, curr_pos):
    first_parameter = parameter_mode(intcode, instruction[1], intcode[curr_pos+1])
    second_parameter = parameter_mode(intcode, instruction[0], intcode[curr_pos+2])

    if first_parameter == second_parameter:
        return 1
    else:
        return 0



def run_intcode_computer(intcode_input = PUZZLE_INPUT.copy()):
    current_position = 0

    while current_position < len(intcode_input):
        operation = intcode_input[current_position]
        print(operation)
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

            intcode_input[output_position] = INPUT_VALUE
            current_position += 2

        elif operation == 4:
            output_position = intcode_input[current_position+1]

            print(f'OPCODE4: {intcode_input[output_position]}')
            current_position += 2

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
    return intcode_input

print(run_intcode_computer())
