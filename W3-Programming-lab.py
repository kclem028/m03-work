#7.4 (Make a list with these 3 strings as elements)

things = ["mozzarella", "cinderella", "salmonella"]

print(things)

#7.5 The "cinderella" element has been replaced with the capitalized version.

things[1] = "Cinderella"

print(things)

#7.6 Printing the capitalized 1st part of the list

print(things[0].upper())
print(things)

#7.7 Deleting Salmonella from the list

del things[2]

print(things)

#9.1 - Defining and printing a list of GOOD

def print_good(good):
    return good

good = ["Harry", "Ron", "Herimone"]

print(good)

#9.2 Generating odd numbers

def get_odds():
    for number in range(10):
        if number % 2 ==1:
            yield number

odd_counter = 0
for odd in get_odds():
    odd_counter += 1
    if odd_counter == 3:
        print("The third odd number is ", odd)
        break