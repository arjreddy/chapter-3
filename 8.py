import math
number_of_people = int(input("Number of people: "))
hot_dog_per_person = int(input("Number of hot dogs per person: "))

total_hot_dogs_needed = number_of_people * hot_dog_per_person

total_hot_dog_buns_needed = 2 * total_hot_dogs_needed

min_hot_dogs_package_needed = math.ceil(total_hot_dogs_needed/10)
min_hot_dog_buns_package_needed = math.ceil(total_hot_dog_buns_needed/8)

print("The minimum number of packages of hot dogs required", min_hot_dogs_package_needed)
print("The minimum number of packages of hot dog buns required", min_hot_dog_buns_package_needed)
print("The number of hot dogs that will be left over", (10*min_hot_dogs_package_needed)-total_hot_dogs_needed)
print("The number of hot dog buns that will be left over", (8*min_hot_dog_buns_package_needed)-total_hot_dog_buns_needed)
