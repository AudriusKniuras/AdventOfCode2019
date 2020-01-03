
houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def recursive_function(houses):
    if len(houses) == 1:
        house = houses[0]
        print(house)
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        recursive_function(first_half)
        recursive_function(second_half)

recursive_function(houses)