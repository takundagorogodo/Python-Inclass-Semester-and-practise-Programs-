import json  # Import the JSON module to work with JSON data

# Create a Python dictionary (data stored in memory)
person = {
    "firstname": "takunda",
    "age": 30,
    "city": "new york",
    "hasChildren": False,
    "titles": ["engineer", "programmer", "developer"]
}

# Convert the Python dictionary into a formatted JSON string
# json.dumps() → Python object to JSON string
personJSON = json.dumps(person, indent=4, sort_keys=True)

# Print the JSON string to the console
print("JSON string output:")
print(personJSON)

# Write the Python dictionary to a JSON file
# json.dump() → Python object to JSON file
with open("person.json", "w", encoding="utf-8") as file:
    json.dump(person, file, indent=4, sort_keys=True)

print("\nJSON data has been written to person.json")

# Convert the JSON string back into a Python dictionary
# json.loads() → JSON string to Python object
person = json.loads(personJSON)

# Print the Python dictionary
print("\nPython dictionary after loading JSON:")
print(person)

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
user = User('Max',27)

#def encode_user(o):
#    if isinstance(o , User):
#        return {'name': o.name , 'age': o.age , o.__class__.__name__: True }
#    else:
#        raise TypeError("Object of the type User is not JSON serialazable")
#
#userJSON = json.dumps(user, default=encode_user)
#print(userJSON)
#
from json import JSONEncoder
class UserEncoder (JSONEncoder):
    def  default(self, o):
         if isinstance(o , User):
           return {'name': o.name , 'age': o.age , o.__class__.__name__: True }
         return JSONEncoder.default(self, o)
        
         
#userJSON = json.dumps(user, cls=UserEncoder)
userJSON = UserEncoder ().encode(user)
print(userJSON)

def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    return dict

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)

