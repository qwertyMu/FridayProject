
#VARIABLES & DATA TYPES

name = "Beki" #String
beki_age = 22 #Integer
ben_age = 42.5 #Float
bank_balance = 35478.98987 #Float
is_female = True #Boolean

#OPERATIONS

result = 10
result = beki_age + ben_age
result = beki_age - ben_age

# print(result)

#Lists & Loops & Functions

cars = ["Ford Focus", "VW Polo", "Suzuki Swift", "Porsche", "Vauxhall Zafira", "Ford Ka"]

def loopThroughCarsList():
    for car in cars:
        print(car)

loopThroughCarsList()

cars.append("Toyota Auris")
cars.remove("Ford Ka")
print()

loopThroughCarsList()


#Conditional Logic

print("---NEW Conditional Logic PROGRAM--")

listOfPeople = ["Sophie", "Luke", "Nick", "Beki", "Paul", "Ben"]

def loopThroughPersonInListOfPeople():
    for person in listOfPeople:
        print(person)

loopThroughPersonInListOfPeople()

print("Dealing with Sophie")

sophies_clothes = input("Please describe your clothing... ")
sophie_age = 25
is_drunk = False

def checkForEntry():
    if is_drunk == True:
        print("Sorry, you're drunk, no entry")
    else:
        if sophie_age >= 18:
            print("Cool you're wearing " + sophies_clothes + " come on in")
        else:
            print("Sorry you're too young")
        
checkForEntry()

name = input("What's your name?")
if name in listOfPeople:
    print("hello " + name)
else:
    print("Sorry " + name + " your not on the list")










