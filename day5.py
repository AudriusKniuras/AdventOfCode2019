PUZZLE_INPUT = [3,225,1,225,6,6,1100,1,238,225,104,0,1001,152,55,224,1001,224,-68,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,62,41,225,1101,83,71,225,102,59,147,224,101,-944,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,2,40,139,224,1001,224,-3905,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1101,6,94,224,101,-100,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1102,75,30,225,1102,70,44,224,101,-3080,224,224,4,224,1002,223,8,223,1001,224,4,224,1,223,224,223,1101,55,20,225,1102,55,16,225,1102,13,94,225,1102,16,55,225,1102,13,13,225,1,109,143,224,101,-88,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1002,136,57,224,101,-1140,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,101,76,35,224,1001,224,-138,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,374,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,389,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,404,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,419,1001,223,1,223,8,226,677,224,102,2,223,223,1005,224,434,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,449,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,479,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,494,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,524,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,539,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,554,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,569,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,584,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,599,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,614,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,629,101,1,223,223,107,226,677,224,102,2,223,223,1006,224,644,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]
TEST_INPUT = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]




####### PART 1 #######
INPUT_VALUE = 5
PUZZLE_INPUT = TEST_INPUT

def parameter_mode(intcode, mode, parameter):
    if mode == '0':
        return intcode[parameter]
    elif mode == '1':
        return parameter


def run_intcode_computer(intcode_input = PUZZLE_INPUT.copy()):
    current_position = 0

    while current_position < len(intcode_input):
        operation = intcode_input[current_position]

        if operation == 1:
            first_input_position = intcode_input[current_position+1]
            second_input_position = intcode_input[current_position+2]
            output_position = intcode_input[current_position+3]
            
            intcode_input[output_position] = intcode_input[first_input_position] + intcode_input[second_input_position]
            current_position += 4
        elif operation == 2:
            first_input_position = intcode_input[current_position+1]
            second_input_position = intcode_input[current_position+2]
            output_position = intcode_input[current_position+3]

            intcode_input[output_position] = intcode_input[first_input_position] * intcode_input[second_input_position]
            current_position += 4
        elif operation == 3:
            output_position = intcode_input[current_position+1]

            intcode_input[output_position] = INPUT_VALUE
            current_position += 2
        elif operation == 4:
            output_position = intcode_input[current_position+1]

            print(f'OPCODE4: {intcode_input[output_position]}')
            current_position +=2
        elif operation == 5:
            first_input_position = intcode_input[current_position + 1]
            second_input_position = intcode_input[current_position + 2]
            if intcode_input[first_input_position] != 0:
                current_position = intcode_input[second_input_position]
            else:
                current_position += 3
        elif operation == 6:
            first_input_position = intcode_input[current_position + 1]
            second_input_position = intcode_input[current_position + 2]
            if intcode_input[first_input_position] == 0:
                current_position = intcode_input[second_input_position]
            else:
                current_position += 3
        elif operation == 7:
            output_position = intcode_input[current_position+3]
            first_input_position = intcode_input[current_position + 1]
            second_input_position = intcode_input[current_position + 2]
            if intcode_input[first_input_position] < intcode_input[second_input_position]:
                intcode_input[output_position] = 1
            else:
                intcode_input[output_position] = 0
            current_position += 4
        elif operation == 8:
            output_position = intcode_input[current_position+3]
            first_input_position = intcode_input[current_position + 1]
            second_input_position = intcode_input[current_position + 2]
            if intcode_input[first_input_position] == intcode_input[second_input_position]:
                intcode_input[output_position] = 1
            else:
                intcode_input[output_position] = 0
            current_position += 4

        elif len(str(operation)) > 1 and operation != 99:
            instruction = list(str(operation))
            while len(instruction) < 5:
                instruction.insert(0,"0")
            if instruction[4] == "1":
                output_position = intcode_input[current_position+3]
                intcode_input[output_position] = parameter_mode(intcode_input, instruction[2], intcode_input[current_position+1]) + parameter_mode(intcode_input, instruction[1], intcode_input[current_position+2])
                current_position += 4
            elif instruction[4] == "2":
                output_position = intcode_input[current_position+3]
                intcode_input[output_position] = parameter_mode(intcode_input, instruction[2], intcode_input[current_position+1]) * parameter_mode(intcode_input, instruction[1], intcode_input[current_position+2])
                current_position += 4
            elif instruction[4] == "5":
                first_parameter = parameter_mode(intcode_input, instruction[2], intcode_input[current_position+1])
                second_parameter = parameter_mode(intcode_input, instruction[1], intcode_input[current_position+2])
                if first_parameter != 0:
                    current_position = second_parameter
                else:
                    current_position += 3
            elif instruction[4] == "6":
                first_parameter = parameter_mode(intcode_input, instruction[2], intcode_input[current_position+1])
                second_parameter = parameter_mode(intcode_input, instruction[1], intcode_input[current_position+2])
                if first_parameter == 0:
                    current_position = second_parameter
                else:
                    current_position += 3
            elif instruction[4] == "7":
                first_parameter = parameter_mode(intcode_input, instruction[2], intcode_input[current_position+1])
                second_parameter = parameter_mode(intcode_input, instruction[1], intcode_input[current_position+2])
                third_parameter = intcode_input[current_position+3]
                #third_parameter = parameter_mode(intcode_input, instruction[0], intcode_input[current_position+3])
                if first_parameter < second_parameter: 
                    intcode_input[third_parameter] = 1
                else:
                    intcode_input[third_parameter] = 0
                current_position += 4
            elif instruction[4] == "8":
                first_parameter = parameter_mode(intcode_input, instruction[2], intcode_input[current_position+1])
                second_parameter = parameter_mode(intcode_input, instruction[1], intcode_input[current_position+2])
                third_parameter = intcode_input[current_position+3]
                #third_parameter = parameter_mode(intcode_input, instruction[0], intcode_input[current_position+3])
                if first_parameter == second_parameter: 
                    intcode_input[third_parameter] = 1
                else:
                    intcode_input[third_parameter] = 0
                current_position += 4

        elif operation == 99:
            break
        else:
            print("LOOP")
            break
    return intcode_input

print(run_intcode_computer())
