'''
Step 4: Your basic practice problem
Scenario: Application User Preferences
A software application stores these user preferences:
user_preferences = {    "theme": "Dark",    "language": "English",    "notifications": True}


The application wants to ensure a font-size preference exists for every user.
Requirements
1. Use setdefault() to add "font_size" with the default value "Medium".
2. Store the returned value in a variable and print it.
3. Use setdefault() on the existing "theme" key with "Light" as the default value.
4. Print the returned value.
5. Print the final dictionary.
6. Print the number of preferences using len().
Rules
- Use setdefault() for both operations.
- Don't use if, else, or loops.
- Don't manually insert or update dictionary entries.
- Write the complete program yourself.
Think carefully about requirement 3: The theme is already "Dark". Will setdefault() change it to "Light"?
'''

user_preferences = {
    "theme": "Dark",
    "language": "English",
    "notifications": True
}

inserted_key = user_preferences.setdefault("font_size","Medium")  # added font_size key and value pair

print(inserted_key)  # printing the value font_size key

theme_request = user_preferences.setdefault("theme", "Light") 
print(theme_request)
''' Main purpose of setdefault is to to check whther the key exist in the dict, if yes print the value, if not it will insert the key with the given value
but here key is already carrying a value Dark in dictionary, now if we give a new value Light, it won't update because key has already a value and 
it will return Dark as ouput'''

print(user_preferences)
print(len(user_preferences))