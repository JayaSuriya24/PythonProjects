# valid dictionary
# integer as a key
my_dict = {1: "one", 2: "two", 3: "three"}
print(my_dict)

# valid dictionary
# tuple as a key
my_dict0 = {(1, 2): "one two", 3: "three"}
print(my_dict0)

# invalid dictionary
# Error: using a list as a key is not allowed
#my_dict1 = {1: "Hello", [1, 2]: "Hello Hi"}

# valid dictionary
# string as a key, list as a value
#my_dict2 = {"USA": ["Chicago", "California", "New York"]}