def add_surname(names):
    return [name + " Kardashian" for name in names if name[0] == "K"]

# Example usage:
names_list = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
print(add_surname(names_list))
