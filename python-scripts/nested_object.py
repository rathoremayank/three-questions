import json 

obj_string = input("Enter a valid JSON object String: ")
key_string = input("Enter a valid Key String: ")

# obj_string = '{"a":{"b":{"c":{"d":"e"}}}}'
# key_string = 'a/b/c/d'

def get_key_value(obj_string, key_string):
    key_string = key_string.replace("/", "")
    keys_list = list()
    keys_list.extend(key_string)

    # converting object string to dictionary
    json_obj = json.loads(obj_string)
    
    #logic for popping items
    ctr = 0 
    
    while ctr < len(keys_list):
        json_obj = json_obj[keys_list[ctr]]
        ctr = ctr + 1

    return json_obj


# function called here

print(get_key_value(obj_string,key_string))
