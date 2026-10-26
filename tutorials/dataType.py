# DATA TYPES

# str
# this is how to declare a multiple line string in python 
# funny_quote = """Jesus you are the mighty man of war
# Jesus you will never ever fall
# when you say it, you will do it"""
# print(funny_quote)

# float 
# when you do / between two number it return a float output auto..ly, but if you whan it to return an interger you do this //
# subj_num = 3

# total_score = 80 + 90 + 92

# average_score =  total_score / subj_num

# print(average_score)

# range(): A built-in type that generates a sequence of numbers, used like a Go loop counter.
# list(): An ordered, changeable collection of items, exactly like a Go slice but can hold mixed types.
# tuple(): An ordered, unchangeable (immutable) collection, like a read-only array that cannot be modified.



nigerian_states = {
    "Abia": "Umuahia",
    "Adamawa": "Yola",
    "Akwa Ibom": "Uyo",
    "Anambra": "Awka",
    "Bauchi": "Bauchi",
    "Bayelsa": "Yenagoa",
    "Benue": "Makurdi",
    "Borno": "Maiduguri",
    "Cross River": "Calabar",
    "Delta": "Asaba",
    "Ebonyi": "Abakaliki",
    "Edo": "Benin City",
    "Ekiti": "Ado-Ekiti",
    "Enugu": "Enugu",
    "Gombe": "Gombe",
    "Imo": "Owerri",
    "Jigawa": "Dutse",
    "Kaduna": "Kaduna",
    "Kano": "Kano",
    "Katsina": "Katsina",
    "Kebbi": "Birnin Kebbi",
    "Kogi": "Lokoja",
    "Kwara": "Ilorin",
    "Lagos": "Ikeja",
    "Nasarawa": "Lafia",
    "Niger": "Minna",
    "Ogun": "Abeokuta",
    "Ondo": "Akure",
    "Osun": "Osogbo",
    "Oyo": "Ibadan",
    "Plateau": "Jos",
    "Rivers": "Port Harcourt",
    "Sokoto": "Sokoto",
    "Taraba": "Jalingo",
    "Yobe": "Damaturu",
    "Zamfara": "Gusau"
}

states = []
capitals = []

for key, value in nigerian_states.items():

    states.append(key)
    capitals.append(value)
    
state_populations = {
    "Kano": 15.0,
    "Lagos": 16.5,
    "Anambra": 5.5,
    "Oyo": 8.0,
    "Borneo": 6.0,
    "Rivers": 7.5,
    "Kaduna": 9.5
}

# Task 1: Basic Loop & Formatting (Perfect!)
for state, population in state_populations.items():
    print(f"The population of {state} is {population} million.")

print("-" * 30)

# Task 2: Conditional Filtering (Awesome List Comprehension!)
states = [state for state, population in state_populations.items() if population > 8.0]
print("States over 8 million:", states)

print("-" * 30)

# Task 3: The Geopolitical Zone Dictionary (Fixed Lookup)
state_zones = {
    "Kano": "North West",
    "Kaduna": "North West",
    "Lagos" : "South West",
    "Oyo" : "South West",
    "Anambra" : "South East",
    "Borneo" : "North East",
    "Rivers" : "South South"
}

for state, population in state_populations.items():
    # Look up the specific zone for the current state
    zone = state_zones[state] 
    print(f"{state} is in the {zone} zone and has {population} million people.")
