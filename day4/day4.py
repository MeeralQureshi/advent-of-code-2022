def read_input_file():
    file_input = open("day4_input.txt", "r")
    read_file = file_input.read()
    parsed_input = read_file.split('\n')
    return parsed_input

def solve_problem():
    input = read_input_file() # Expected 4
    overlapping_pairs = 0
    # Step 1: Loop through input and get first and second pair
    for pairs in input:
        pairs = pairs.split(',')
        first_elf = pairs[0].split('-')
        second_elf = pairs[1].split('-')
        # Step 2: For each elf create a list containing all the sections they are working on
        first_elf_sections = [section for section in range(int(first_elf[0]), int(first_elf[1]) + 1)]
        second_elf_sections = [section for section in range(int(second_elf[0]), int(second_elf[1]) + 1)]
    # Step 3: See if elf 1 sections contain elf 2 and vice versa
        check_first_elf_to_second = any(section in first_elf_sections for section in second_elf_sections)
    # Step 4: If so increment the overlapping number of pairs
        if check_first_elf_to_second:
            overlapping_pairs += 1
    return overlapping_pairs
    

answer = solve_problem()
print(answer)