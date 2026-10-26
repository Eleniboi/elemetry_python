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
