#Task 1
first_name ="Hasiyatu"
last_name ="Ismail"
age =21
favourite_programming_concept ="Functions"

print("first_name:", first_name)
print("last_name:", last_name)
print("age:", age)
print("favourite_programming_concept:", favourite_programming_concept)

#Task 2
full_name = first_name + " " + last_name
print(full_name)

full_name = f"{first_name} {last_name}"
print(full_name)


#Task 3
print(full_name.upper())

print(full_name.lower())

print(full_name.lower().count("a"))


print(full_name.find(" "))


print(full_name.replace(first_name, "Coder"))

#Task 4
print(f"Hey I go by the name {full_name}, I am {age} years old and my favourite concept so far is {favourite_programming_concept}")


#Task 5

print(full_name[0])
print(full_name[-1])
print(full_name[0:8])