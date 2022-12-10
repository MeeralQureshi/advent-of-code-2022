import string

def read_input_file():
    file_input = open("day3_input.txt", "r")
    read_file = file_input.read()
    parsed_input = read_file.split('\n')
    return parsed_input

def solve_problem():
    input = read_input_file() # Expected 70
    # Step 1: Create a priority dictionary for a-z and A-Z
    priority_scores = {}
    letters_list = list(string.ascii_letters)
    sum_priorities = 0
    for i in range(len(letters_list)):
        priority_scores[letters_list[i]] = i + 1
    i = 0
    # Step 2: Loop through the rucksack and compare values between the next 2 elves
    while i < len(input):
        first_rucksack = input[i]
        second_rucksack = input[i + 1]
        third_rucksack = input[i + 2]
        for item in first_rucksack:
            # Step 3: If item is matching between all 3 elves we want to add this to the priority sum
            if item in second_rucksack and item in third_rucksack:
                sum_priorities += priority_scores[item]
                break
        i += 3

    return sum_priorities
    

answer = solve_problem()
print(answer)