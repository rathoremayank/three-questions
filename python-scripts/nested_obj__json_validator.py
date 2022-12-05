import json 

obj_string = input("Enter a valid JSON object String: ")
key_string = input("Enter a valid Key String: ")

def validate_json_obj(obj_string):
    try:
        json.loads(obj_string)
    except ValueError as err:
        return False
    return True

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


# functions called here
if validate_json_obj(obj_string):
    print("Object String is a valid JSON! Proceeding..")
    print("Value is:", get_key_value(obj_string,key_string))
