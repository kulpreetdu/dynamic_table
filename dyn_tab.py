import json
import pandas as pd

# Data to be written
dictionary = {
"name": ["Bob","George"],
"age": [20,42]
}
# Writing JSON file
with open("data.json", "w") as outfile:
    json.dump(dictionary, outfile)
# Opening JSON file
with open('data.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))

#Converting into Dataframe
json_object = pd.DataFrame(json_object)
print(type(json_object))
# Introducing gender value as dictionary
gender1 = {20:"male",42:"male"}
# Mapping the dictionary keys to the data frame.
json_object['gender'] = json_object['age'].map(gender1)

print(json_object)

#Inserting new values into teh dataframe
new_data={"name":["Sara","Conor","Jennifer"],
        "age": [42,40,42],
        "gender":["female","male","female"]}
new_data = pd.DataFrame(new_data)

#merging the existing dataframe in the the new dataframe
json_object = pd.concat([json_object, new_data], ignore_index = True)
json_object.reset_index()
json_object = pd.DataFrame(json_object)
print(json_object)