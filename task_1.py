list = [4,5,9,6,8,2,7]
print(list)

#append the list
list.append(10)
print(list)

#removing the element 5 from the list
list.remove(5)
print(list)

# pop the element at index 2 
list.pop(2)
print(list)

#updating the element at index 1
list[1] = 16
print(list)

# dictionary

my_dict = {"name": "akul", "age": "10", "country": "india" }
print(my_dict)

# modifying the existing value 
my_dict["age"] = "12"
print(my_dict)

# adding a new key value pair
my_dict["city"] = "pune"
print(my_dict)

# removing a key value pair
del my_dict["age"]
print(my_dict)

# updating the key value pair
my_dict.update({"country": "germany", "city":"berlin"})
print(my_dict)

# set

set = {10,20,30}
print(set)
# adding an element
set.add(40)
print(set)
# update the element
set.update([50,60])
print(set)
#remove an element
set.remove(30)
print(set)

# union operation 
set1 = {1,5,6,2}
set2 = {2,5,8,9}
result = set1 | set2
print(result)

# intersect operation 
result = set1 & set2
print(result)