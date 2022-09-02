from Animal import Animal, Fish, Dog, Lion, Shark
from enum import Enum
from colorama import Fore, Style, Back
import os

class Actions(Enum):
    ADD = 1
    DELETE = 2
    SEARCH = 3
    PRINT = 4
    EXIT = 5

class AnimalType(Enum):
    DOG = 1
    LION = 2
    FISH = 3
    SHARK = 4

def menu():
    print(Fore.LIGHTGREEN_EX + 'Welcome to the "Stupid Zoo"!' + Style.RESET_ALL)
    print(Fore.RED + 'Please view all available selections.' + Style.RESET_ALL)
    for option in Actions:
        print(f'{option.value} - {option.name}')
    user_selection = input(Fore.CYAN + "Please enter your selection: " + Style.RESET_ALL)
    return int(user_selection)

def animal_type():
    print(Fore.GREEN + 'Please view all available selections.' + Style.RESET_ALL)
    for an_tp in AnimalType:
        print(f'{an_tp.value} - {an_tp.name}')
    user_selection = input(Fore.LIGHTYELLOW_EX + "Please enter your selection: " + Style.RESET_ALL)
    return(int(user_selection))

def add_animal(my_zoo):
    kind_of_animal = animal_type()
    print(Back.GREEN + "Added successfully!" + Style.RESET_ALL)
    if kind_of_animal == AnimalType.DOG.value:
        my_zoo.append(Dog("Lilly", 2))
        print("Fun fact about dogs:")
        return Dog.bark(Dog), print()
    if kind_of_animal == AnimalType.LION.value:
        my_zoo.append(Lion("Simba", 3))
        print("Fun fact about lions:")
        return Lion.roar(Lion), print()
    if kind_of_animal == AnimalType.FISH.value:
        my_zoo.append(Fish("Nemo", 4))
        print("Fun fact about fish:")
        return Fish.swim(Fish), print()
    if kind_of_animal == AnimalType.SHARK.value:
        my_zoo.append(Shark("Jaws", 60))
        print("Fun fact about sharks:")
        return Shark.devour(Shark), print()

def print_all(my_zoo): 
    for allzoo in my_zoo:
        print(allzoo)

def search_animals(my_zoo):
    animal_2_search = input("Animal's Name? ")
    for x in my_zoo: 
        if x.name == animal_2_search:
            print(x)
            
def main():
    my_zoo = []
    user_selection = menu()
    os.system("clear")
    while user_selection != Actions.EXIT.value:
        if user_selection == Actions.ADD.value:
            add_animal(my_zoo)
        if user_selection == Actions.DELETE.value:
            pass
        # delete_animal(my_zoo)
        if user_selection == Actions.SEARCH.value:
            search_animals(my_zoo)
        # search_animal(my_zoo)
        if user_selection == Actions.PRINT.value:
            print_all(my_zoo)
        # print_animals(my_zoo)
        user_selection = menu()
    print(Fore.MAGENTA + "Thank you for using this software. Goodbye!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
