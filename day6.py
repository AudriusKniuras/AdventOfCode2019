import sys

#PUZZLE_INPUT = open('day6_part2.in').read()
PUZZLE_INPUT = open('day6.in').read()
PUZZLE_INPUT = PUZZLE_INPUT.split('\n')

def find_root(nodes = PUZZLE_INPUT):
    root = nodes[0].split(')')[0]
    root_found = False
    while (root_found == False):
        previous_root = root
        for orbit in nodes:
            first_part, second_part = orbit.split(')')
            if second_part == root:
                previous_root = root
                root = first_part
        if previous_root == root:
            root_found = True
    return root

def find_branches(root_branch, nodes = PUZZLE_INPUT):
    branches = {root_branch: []}
    for node in nodes:
        first_part, second_part = node.split(')')
        if first_part == root_branch:
            branches[root_branch].append(second_part)
    return branches

def find_parent_node(child_branch, nodes = PUZZLE_INPUT):
    branches = {child_branch: []}
    for node in nodes:
        first_part, second_part = node.split(')')
        if second_part == child_branch:
            branches[child_branch].append(first_part)
    return branches

total_distance = 0
distance_from_the_root = 0
parent_distance = {}
parent_array = []

def visit_branches(node, nodes = PUZZLE_INPUT):
    global distance_from_the_root
    global total_distance
    global parent_distance
    global parent_array

    distance_from_the_root += 1
    parent_array.append(node)
    # dictionary {node:[branch1,branch2]} {E:[F,J]}
    node_with_branches = find_branches(node)
    # array of branches [F,J]
    branches = node_with_branches[node]
    
    if len(branches) == 1:
        total_distance += distance_from_the_root
        visit_branches(branches[0])
    elif len(branches) == 2:
        total_distance += distance_from_the_root
        parent_distance[node] = distance_from_the_root-1

        visit_branches(branches[0])

        distance_from_the_root += 1
        
        total_distance += distance_from_the_root
        
        visit_branches(branches[1])

        del parent_distance[list(parent_distance.keys())[-1]]
        if len(parent_distance.keys()) > 0:
            distance_from_the_root = parent_distance[list(parent_distance.keys())[-1]]
        
    elif len(branches) == 0: 
        
        distance_from_the_root -= 1
        if node == "SAN":
            print(f"SAN distance from the root: {distance_from_the_root}")
            print(f"Parent array: {parent_array}")
                    

        
        # print(f'Current orbit: {node_with_branches}')
        # print(f'Distance from the root: {total_distance}')
        # distance between E (parent) and F(last child)
        parent_last_child_distance = distance_from_the_root - parent_distance[list(parent_distance.keys())[-1]]
        distance_from_the_root -= parent_last_child_distance


    

#visit_branches('COM')
#print(total_distance)


######### PART 2 ##########

YOU_parent_node = find_parent_node('YOU')

visited_branches = []
path_to_santa = []
steps_taken = 0
def find_santa(node):
    global visited_branches
    global steps_taken
    global path_to_santa
    # dict {NODE: PARENT}
    parent_child_dict = find_parent_node(node)
    # dict {NODE: [CHILD1, CHILD2]}
    node_with_branches = find_branches(list(parent_child_dict.keys())[0])

    # "YOU"
    node = list(node_with_branches.keys())[0]
    # "K"
    if len(parent_child_dict[node]) > 0:
        parent_of_node = parent_child_dict[node][0]
    else:
        return
    # ["BRANCH1", BRANCH2]
    child_branches = node_with_branches[node]
    #print(f"Current node: {node}")

    if len(child_branches) == 1:
        if child_branches[0] not in visited_branches:
            steps_taken += 1
            visited_branches.append(child_branches[0])
            path_to_santa.append(child_branches[0])
            find_santa(child_branches[0])       
        else:
            find_santa(parent_of_node)
    if len(child_branches) == 2:
        not_visited = []
        for branch in child_branches:
            if branch not in visited_branches:
                not_visited.append(branch)
        if len(not_visited) > 0:
            for not_visited_branch in not_visited:
                steps_taken += 1
                visited_branches.append(not_visited_branch)
                path_to_santa.append(not_visited_branch)
                find_santa(not_visited_branch)   
        else:
            find_santa(parent_of_node)

    if len(child_branches) == 0:
        if node == "SAN":
            #print(f"SANTA FOUND, orbit {parent_child_dict}")
            print(f"part2STEPS TAKEN: {len(path_to_santa)}")
        else:
            if node in path_to_santa:
                path_to_santa.remove(node)
            visited_branches.append(node)
            find_santa(parent_of_node)

#visit_branches("COM")

orbits = {x.split(')')[1]:x.split(')')[0] for x in PUZZLE_INPUT}

you_orbit = "YOU"
san_orbit = "SAN"

you_orbits = []
san_orbits = []

while you_orbit in orbits:
    you_orbits.append(orbits[you_orbit])
    you_orbit = orbits[you_orbit]

while san_orbit in orbits:
    san_orbits.append(orbits[san_orbit])
    san_orbit = orbits[san_orbit]

transfer_count = min([you_orbits.index(orbit) + san_orbits.index(orbit) for orbit in set(you_orbits) & set(san_orbits)])
print(f"Part2: {transfer_count}")

