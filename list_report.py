items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

print("Shopping List:")
for index in range(len(items)):
    print(f"{index + 1}. {items[index]}")

count = 0

for item in items:
    if len(item) > 4:
        count += 1

longest = items[0]

for item in items:
    if len(item) > len(longest):
        longest = item

print("Items with more than 4 letters:", count)
print("Longest item:", longest)
