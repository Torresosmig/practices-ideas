
# input list
drink1 = []


def list_drink_ingredients():
    drink_list = input("\nDo you want the list of the drink?  y/n  ")
    if drink_list == 'y':
        drink1.remove(name_drink1)
        print("The ingredients of drink ", name_drink1, " are: ", drink1)

    elif drink_list == 'n':
        print("\nOh well...")
# ask for ingredients name


def add_ingredient():
    ingredient = input("\nEnter name of ingredient: ")
    drink1.append(ingredient)  # adds input to drink1 list


def find_another():

    finder = input("\ndo you want to find another ingredient? y/n  ")
    if finder == 'y':
        another_ingredient = input("\nIngredient's name to find?  ")

        if another_ingredient in drink1:

            print("\nIngredient ", another_ingredient, " found in drink ", name_drink1)

        else:

            print("\nIngredient ", another_ingredient, " not found in drink ", name_drink1)
            find_another()
    elif finder == 'n':
        pass
    else:
        print("\nCouldn't understand...")
        find_another()


print("\nWith this program you can make list ingredients of a drink")
print("then you can search if a certain ingredient is contained in a drink\n")

print("1. First name the drink")
name_drink1 = input("\nName of drink? ")
drink1.append(name_drink1)


def find():

    while True:

        add_ingredient()
        choice = input("\nEnter 'y' to stop, press any to continue... ")
        if choice == 'y':
            break

        choice = input("\ndo you want to find any ingredient? y/n  ")
        if choice == 'y':
            ingredient_name = input("\nIngredient's name to find?  ")
            if ingredient_name in drink1:

                print("\nIngredient ", ingredient_name, " found in drink ", name_drink1)
                find_another()

            else:
                print("\nIngredient ", ingredient_name, " not found in drink ", name_drink1)
                find_another()

        elif choice == 'n':
            choice = input("\ndo you want to add ingredient instead? y/n  ")

            if choice == 'y':
                add_ingredient()
                choice = input("\nEnter 'y' to stop, press any to continue... ")
                if choice == 'y':
                    break

            elif choice == 'n':
                print("\nOh well I'll see you soon...\n")
                break
        else:
            print("\nNo valid answer")
            find_another()


find()
