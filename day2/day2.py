def read_input_file():
    file_input = open("day2_input.txt", "r")
    read_file = file_input.read()
    parsed_input = read_file.split('\n')
    return parsed_input

def solve_problem():
    # Expected is 15
    input = read_input_file()
    # Step 1: Figure out opponent move and then your move
    # A = Rock - 1
    # B = Paper - 2 
    # C = Scissors - 3
    # X = Lose = 0
    # Y = Draw = 3
    # Z = Win = 6
    moves = {
        'A': {
            'X': 3,
            'Y': 4,
            'Z': 8,
        },
        'B': {
            'X': 1,
            'Y': 5,
            'Z': 9,
        },
        'C': {
            'X': 2,
            'Y': 6,
            'Z': 7,
        },
    }
    total_score = 0
    # Step 2: Map the number of points based on the round
    for round in input:
        opponents_move = round[0]
        outcome = round[2]
        total_score += moves[opponents_move][outcome]
    # Step 3: Sum these points together
    return total_score

answer = solve_problem()
print(answer)