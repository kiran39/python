print("kiran")
# list operations like deleting data
data = [4, 5, 104, 105, 110, 120, 130, 150, 160,
        170, 183, 187, 191, 350, 360]
min_value = 100
max_value = 200
#process the list to contain items in between min_value and max_value

stop = 0
for index, value in enumerate(data):
    if value >= min_value:
        stop = index
        break
print(stop)
del data[:stop]
print(data)
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_value:
        start = index + 1
        break
del data[start:]
print(data)