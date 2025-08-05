lucky_numbers = [4, 8, 15, 16, 56, 23 ]

friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim", "Jim", "Jim", "Jim"]


friends.extend(lucky_numbers)
friends.append("John")

friends.insert(2, "Paul")

print(friends)
print(friends.index("Karen"))
print(friends.count("Jim"))

lucky_numbers.sort()
print(lucky_numbers)
