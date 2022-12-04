def read_input_file():
    file_input = open("day1_input.txt", "r")
    read_file = file_input.read()
    parsed_input = read_file.split('\n')
    return parsed_input

def solve_problem():
    input = read_input_file()
    # Setup a list to get max later
    elf_calories = []
    calories_sum = 0
    # Step 1: Loop through all the calories
    for calories in input:
        if calories == '':
            # Step 2: If empty string, add sum to list
            elf_calories.append(calories_sum)
            calories_sum = 0
        else:
            # Step 2: If number, convert to a number and add to sum
            calories_sum += int(calories)
    elf_calories.append(calories_sum)
    # Step 3: To get max 3, sort the array and sum the last 3 values
    elf_calories.sort()
    return sum(elf_calories[-3:])

answer = solve_problem()
print(answer)