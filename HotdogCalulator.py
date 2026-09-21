'''Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a program that calculates the number of packages of hot dogs and the number 
of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask the user for the number of people attending the 
cookout and the number of hot dogs each person will be given. The program should display the following details:
The minimum number of packages of hot dogs required
The minimum number of packages of hot dog buns required
The number of hot dogs that will be left over
The number of hot dog buns that will be left over'''

 HOTDOG_PER_PACKAGE = 10
 BUNS_PER_PACKAGE = 8

people_count = int(input("How many people will attend the cookout?: ")
hotdog_count = int(input("How many hotdogs per person? : ") 

total = people_count * hotdog_count

print(f"The total number of hot dogs are {total}.")



