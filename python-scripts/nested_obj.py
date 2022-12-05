import json 

# obj_string = input("Enter object String: ")
# key_string = input("Enter key String: ")

obj_string = '{"a":{"b":{"c":{"d":"e"}}}}'
key_string = 'a/b/c'

key_string = key_string.replace("/", "")
keys_list = list()
keys_list.extend(key_string)

print("Key list is: ", keys_list)
print(type(keys_list))

# converting object string to dictionary 
json_obj = json.loads(obj_string)

# checking data type of new json_obj 
print(type(json_obj))


#logic for popping items

ctr = 0 

while ctr < len(keys_list):
    json_obj = json_obj[keys_list[ctr]]
    print(json_obj)
    print(keys_list[ctr])
    ctr = ctr + 1

