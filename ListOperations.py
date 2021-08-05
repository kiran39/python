menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
#tip: you can move nested list in list using (alt + shift + up)
for nested_list in menu:
    #reverse the inner list
    for index in range(len(nested_list) - 1, -1, -1):
        if nested_list[index] == "spam":
            del nested_list[index]

print(menu)