# Creating a dictionary of phone numbers
phone_numbers = {
    'Ram': 1234,
    'Shram': 678,
    'Mohan': 111,
    'Shram': 986            # This overwrites the previous 'Shram' value
}

# Creating the same dictionary using dict() constructor
phone_numbers = dict({
    'Ram': 1234,
    'Shram': 678,
    'Mohan': 111,
    'Shram': 986            # Again overwritten
})

# Updating Mohan's phone number
phone_numbers['Mohan'] = 888

# Adding multiple phone numbers for Madhav using a set
phone_numbers['Madhav'] = {1122, 72728, 8987}

# Replacing Ram's number with a nested dictionary (home & work numbers)
phone_numbers['Ram'] = {
    'Ram_Home': 98765,
    'Ram_Work': 235677
}

# Accessing a nested dictionary value
print(phone_numbers['Ram']['Ram_Home'])   # Prints Ram's home number

# Printing the full dictionary
print(phone_numbers)

# Accessing value by key
print(phone_numbers['Shram'])

# Another dictionary with numeric keys
data = {
    1: "taku",
    3: "samue",
    0: "godaz"
}

# Accessing value using numeric key
