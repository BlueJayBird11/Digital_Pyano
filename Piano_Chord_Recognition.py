# creates an empy list which will have the x, y, and z values added to them 
my_list = []

# Asks for user input for which key they would like to play and sets them equal to a respective variable
# Example (x = F), (y = G), (z = D)
x = input("pick a Key ")
y = input("pick a Key ")
z = input("pick a Key ")

# appends values associated with x, y, and z to the list declared at the beginning
my_list.append(x)
my_list.append(y)
my_list.append(z)

# Example of what 'my_list' should look like at this point "['F', 'G', 'D']"
print(my_list)

# This appends every key that is in an octive
my_list.append("C")
my_list.append("C_Sp")
my_list.append("D")
my_list.append("D_Sp")
my_list.append("E")
my_list.append("F")
my_list.append("F_Sp")
my_list.append("G")
my_list.append("G_Sp")
my_list.append("A")
my_list.append("A_Sp")
my_list.append("B")

# Example of what 'my_list' should look like at this point is listed in the line below
# '['F', 'G', 'D', 'C', 'C_Sp', 'D', 'D_Sp', 'E', 'F', 'F_Sp', 'G', 'G_Sp', 'A', 'A_Sp', 'B']'
print(my_list)

# At this point we take a set of 'my list', this insures that the variables (x, y, z) will still
# be present in the set, the excess values will be thrown out as a set can only contain unique values
conversion = set(my_list)

# Example of what 'conversion' should look like at this point is listed in the line below
# '{'B', 'A', 'D_Sp', 'G', 'A_Sp', 'E', 'C_Sp', 'F_Sp', 'D', 'F', 'C', 'G_Sp'}'
print(conversion)

# this simply organizes 'coversion' in alphabetical order, it also simultaneously converts the set back into a list
organizer = sorted(conversion)

# Example of what 'organizer' should look like at this point is listed in the line below
# '['A', 'A_Sp', 'B', 'C', 'C_Sp', 'D', 'D_Sp', 'E', 'F', 'F_Sp', 'G', 'G_Sp']'
print(organizer)

# These two lists are simply place holder lists which will be used to organize the list in a manner according to the first input
list1 = []
list2 = []

# This will break the current filled list 'organizer' in to two seperate lists. One list will befilled with the str values which indeces is equal to or greater than
# the initial x variables index within the list. The other list will be made up of those points which did not meet the given criteria.
for i in range(len(organizer)):
    if i >= organizer.index(x):
        list1.append(organizer[i])
    else:
        list2.append(organizer[i])

# Example of what 'list1' should look like at this point is listed in the line below
# '['F', 'F_Sp', 'G', 'G_Sp']'
print(list1)

# Example of what 'list2' should look like at this point is listed in the line below
# '['A', 'A_Sp', 'B', 'C', 'C_Sp', 'D', 'D_Sp', 'E']'
print(list2)

# This algorithm will simply append each value in 'list2' the end of 'list1'
for i in range(len(list2)):
    list1.append(list2[i])

# Example of what 'list1' should look like at this point is listed in the line below
# ['F', 'F_Sp', 'G', 'G_Sp', 'A', 'A_Sp', 'B', 'C', 'C_Sp', 'D', 'D_Sp', 'E']
print(list1)        
