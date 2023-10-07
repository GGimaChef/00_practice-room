import os

names_starting_with_x = [each_name for each_name in os.listdir() if each_name.startswith("x")]

print(names_starting_with_x)

for each_item in names_starting_with_x:
	print("===============" + each_item)