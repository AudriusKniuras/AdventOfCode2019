PUZZLE_INPUT = open('day6.in').read()
PUZZLE_INPUT = PUZZLE_INPUT.split('\n')

map_dictionary = {}
for orbit in PUZZLE_INPUT:
    first_planet = orbit.split(')')[0]
    second_planet = orbit.split(')')[1]