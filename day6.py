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

total_distance = 0
distance_from_the_root = 0
parent_distance = {}
def visit_branches(node, nodes = PUZZLE_INPUT):
    global distance_from_the_root
    global total_distance
    global parent_distance

    
    # dictionary {node:[branch1,branch2]}
    node_with_branches = find_branches(node)
    # array of branches
    branches = node_with_branches[node]
    distance_from_the_root += 1
    #print(f'branch: {node_with_branches}, Distance: {distance_from_the_root}')
    if len(branches) == 1:
        total_distance += distance_from_the_root
        visit_branches(branches[0])
    elif len(branches) == 2:
        total_distance += distance_from_the_root
        
        parent_distance[node] = distance_from_the_root
        #print(f'Current orbit: {node_with_branches}')
        #print(f'parent distance: {parent_distance[node]}')
        visit_branches(branches[0])
        visit_branches(branches[1])
        
    elif len(branches) == 0: 
        total_parent_distance = 0
        for parent in parent_distance:
            total_parent_distance += parent_distance[parent]
        total_distance += distance_from_the_root + total_parent_distance
        print(f'Current orbit: {node_with_branches}')
        print(f'Distance from the root: {total_distance}')
        distance_from_the_root = 0
        parent_distance = {}

    

visit_branches('COM')
print(total_distance)



# current output = 15405, 30000 is too low
