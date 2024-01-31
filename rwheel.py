#CS-175L
#Gavin Kinsella
#Roulette Wheel Program

num_ask = int(input("Enter a number on a Roulette Wheel: "))
pocket_color = 0

if num_ask >= 0 and num_ask <= 36:
    if num_ask == 0:
        pocket_color = "green"
    elif num_ask >= 1 and num_ask <= 10:
        if num_ask % 2 == 0:
            pocket_color = "black"
        else:
            pocket_color = "red"

    elif num_ask >= 11 and num_ask <= 18:
        if num_ask % 2 == 0:
            pocket_color = "red"
        else:
            pocket_color = "black"

    elif num_ask >= 19 and num_ask <= 28:
        if num_ask % 2 == 0:
            pocket_color = "black"
        else:
            pocket_color = "red"

    elif num_ask >= 29 and num_ask <= 36:
        if num_ask % 2 == 0:
            pocket_color = "red"
        else:
            pocket_color = "black"

    print("Your pocket color is = ", pocket_color)
else:
    print("Error. Number must be between 0 and 36.")


            
