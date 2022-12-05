import json 

# obj_string = input("Enter object String: ")
# key_string = input("Enter key String: ")

obj_string = '{"a":{"b":{"c":{"d":"e"}}}}'
key_string = 'a/b/c'

def get_key_value(obj_string, key_string):
    key_string = key_string.replace("/", "")
    keys_list = list()
    keys_list.extend(key_string)

    # converting object string to dictionary and checking type of it
    json_obj = json.loads(obj_string)
    print(type(json_obj))
    
    #logic for popping items
    ctr = 0 
    while ctr < len(keys_list):
        json_obj = json_obj[keys_list[ctr]]
        print(json_obj)
        ctr = ctr + 1

    return json_obj


# function called here
print(get_key_value(obj_string,key_string))
