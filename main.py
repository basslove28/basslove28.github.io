# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


name = input('Enter your name: ')
print('Hello', name)

iceC = input('Now that I got your name, enter your favorite ice cream: ')
sizeX = input('Whats is the size?: "Type letter for size Small(S), Medium(M), Large(L)" ')
topping = input('Do you want any toppings? type y/n ')
many = input('Finally, how many ice creams you are purchasing? ')

sizeS = 1.50
sizeM = 2.50
sizeL = 3.50
topping = .50


if sizeX == "S":
    sizeX = sizeS
elif sizeX == "M":
    sizeX = sizeM
elif sizeX == "L":
    sizeX = sizeL
else:
    print('Try again')

if topping == "y" or "Y":
   total = ((sizeX + topping * many) * .07)
   final = sizeX + total
elif topping == "n" or "N":
   total = ((sizeX * many) * .07)
   final = sizeX + total

print("Your total price for your ", iceC, " is: ", final)

# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#   print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
