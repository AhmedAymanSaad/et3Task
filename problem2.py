TXT_FILE_PATH = "../problem2/image1.txt"

import json
import os

# input the txt file path
TXT_FILE_PATH = input("Please input the txt file path: ")

json_obj_list = []

# read file line by line
with open(TXT_FILE_PATH, 'r') as f:
    lines = f.readlines()

for line in lines:
    # split the line by space
    line_split = line.split(' ')
    rotation = line_split[0]
    x = line_split[1]
    y = line_split[2]
    width = line_split[3]
    height = line_split[4].split('\n')[0]
    # create json object
    json_obj = {
        "image_rotation": float(rotation),
        "value": {
            "x": float(x),
            "y": float(y),
            "width": float(width),
            "height": float(height),
            "rotation": float(rotation),
            "rectanglelabels": [
                "object"
            ]
        }
    }
    json_obj_list.append(json_obj)

result = { "result": json_obj_list }

# change all / to \ in file path
TXT_FILE_PATH = TXT_FILE_PATH.replace('/', '\\')

# write json object to file
file_name = TXT_FILE_PATH.split('\\')[-1].split('.')[0]
# check if file exists
if os.path.exists("./" + file_name + ".json"):
    os.remove("./" + file_name + ".json")
with open("./" + file_name + ".json", 'w') as f:
    json.dump(result, f, indent=4)
