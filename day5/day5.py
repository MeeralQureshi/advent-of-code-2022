import re

def read_input_file():
    file_input = open("day5_input.txt", "r")
    read_file = file_input.read()
    parsed_input = read_file.split('\n')
    return parsed_input

def solve_problem():
    input = read_input_file()
    crates = []
    num_of_stacks = 0
    moves = []
    # Step 1: Parse crates, Find Number of Stacks, Parse Moves
    for line in input:
        if '[' in line:
            crates.append(line)
        elif 'move' in line:
            moves.append(line)
        elif line != '':
            num_of_stacks = int(line[-2])
        
    # Step 2: Build a dictionary out of the stack layout
    stack_layout = {}
    for i in range(num_of_stacks):
        stack_layout[i + 1] = []

    for row in reversed(crates):
        for i in range(num_of_stacks):
            crate_letter_position = (i * 4) + 1
            crate_letter = row[crate_letter_position]
            if crate_letter != ' ':
                stack_layout[i + 1].append(crate_letter)

    # Step 3: Loop over the moves and execute on dictionary
    for move in moves:
        move_values = re.findall(r'\d+', move)
        num_of_crates_to_move = int(move_values[0])
        crates_from = int(move_values[1])
        crates_to = int(move_values[2])
        crates_to_move = stack_layout[crates_from][-num_of_crates_to_move:]
        stack_layout[crates_from] = stack_layout[crates_from][:-num_of_crates_to_move]
        stack_layout[crates_to] += crates_to_move

    top_crates = ''
    # Step 4: For each stack in dictionary, get "top" crate
    for values in stack_layout.values():
        top_crates += values[-1]
    return top_crates
    

answer = solve_problem()
print(answer)