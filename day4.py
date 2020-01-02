INPUT_LOW = 284639
INPUT_HIGH = 748759


####### PART 1 ######

password_count = 0
good_number_arr = []
while INPUT_LOW < INPUT_HIGH+1:
    # check if list and set length are the same
    # set only contains unique elements
    if len(list(str(INPUT_LOW))) == len(set(str(INPUT_LOW))):
        INPUT_LOW += 1
        continue
    else:
        good_number = True
        input_arr = list(str(INPUT_LOW))
        for i in range(len(input_arr)-1):
            if int(input_arr[i]) > int(input_arr[i+1]):
                good_number = False
        if good_number:
            good_number_arr.append(INPUT_LOW)
            password_count += 1
        INPUT_LOW += 1

#print(password_count)
                

##### PART 2 #######



password_count_part2 = 0
good_number_arr_part2 = []
for number in good_number_arr:
    num_str_array = list(str(number))
    same_number_array = []
    for i in range(len(num_str_array)-1):

        if num_str_array[i] == num_str_array[i+1]:
            same_number_array.append(num_str_array[i])
        elif num_str_array[i] != num_str_array[i+1] and len(same_number_array) == 1:
            if number not in good_number_arr_part2:
                print(number)
                password_count_part2 += 1
                good_number_arr_part2.append(number)
                same_number_array = []
        # if 333399, then "if num_str_array[i]" will run 3 times, and same_number_array, will have 3 occurences, 
        # clean that array before moving forward
        elif len(same_number_array) > 1:
            same_number_array = []
    if len(same_number_array) == 1 and number not in good_number_arr_part2:
        print(number)
        password_count_part2 += 1
        good_number_arr_part2.append(number)         

print(password_count_part2)

