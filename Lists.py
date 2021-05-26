vegetables = ["Cabbage", "Lettuce", "Tomato", "Potato"]
print(vegetables[2:4])

vegetables[2] = "poop"
print(vegetables[0:])

list1 = [4543,4323, 12,3232,43]
list2 = ["boosad", "dwdwad", "dwada"]

list2.pop(2)
list2.insert(2,"whgat the shart")
print(list2)
try:
    print(list1.index("21d"))
except ValueError:
    print("There was a value error")

list1.reverse()
print(list1)

friends = ["James","Lewis","George","Tom","Jack"]
friends2 = friends.copy()
print(friends)
print(friends2)

coordinates = [(9, 2), (13, 4)]
print(coordinates[1])