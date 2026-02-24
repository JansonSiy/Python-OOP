# 1. for loop
names = ["polar", "pixie", "leon"]

for name in names:
    print(name)

# OUTPUT
# polar
# pixie
# leon

# ==================================================

# 2. for loop range() - "stop".
for i in range(5):
    print(i)

# OUTPUT
# 0
# 1
# 2
# 3
# 4

# ==================================================

# 3. for loop range() - "start" and "stop".
for i in range(2, 6):
    print(i)

# OUTPUT
# 2
# 3
# 4
# 5

# ==================================================

# 4. for loop range() - "start", "stop" and "step".
for i in range(1, 10, 2):
    print(i)

# OUTPUT
# 1
# 3
# 5
# 7
# 9

for i in range(5, 0, -1):
    print(i)

# OUTPUT
# 5
# 4
# 3
# 2
# 1

# ==================================================

# 5. break
for i in range(10):
    print(i)
    if i == 5:
        break

# OUTPUT
0
1
2
3
4
5

# ==================================================

# 6. continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# OUTPUT
0
1
3
4

# ==================================================

# 7. .items()
names = {1: "polar", 2: "pixie", 3: "leon"}

for key, value in names.items():
    print(key, value)

# OUTPUT
# 1 polar
# 2 pixie
# 3 leon

# ==================================================

# 8. .keys()
names = {1: "polar", 2: "pixie", 3: "leon"}

for key in names.keys():
    print(key)

# OUTPUT
# 1
# 2
# 3

# ==================================================

# 9. .values()
names = {1: "polar", 2: "pixie", 3: "leon"}

for value in names.values():
    print(value)

# OUTPUT
# polar
# pixie
# leon

# ==================================================

# 10. while loop
count = 0

while count < 5:
    print(count)
    count += 1

# OUTPUT
# 0
# 1
# 2
# 3
# 4

# ==================================================

# 11. .enumerate() - with and without "start"
fruits = ["apple", "banana", "apple", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# OUTPUT
# 0 apple
# 1 banana
# 2 apple
# 3 mango

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# OUTPUT
# 1 apple
# 2 banana
# 3 apple
# 4 mango

# ==================================================

# 12. .enumerate() with slicing
fruits = ["apple", "banana", "apple", "mango"]

for index, fruit in enumerate(fruits):
    # fruits[:index] → all elements **before** the current index
    # fruits[index+1:] → all elements **after** the current index (excluding current)
    if fruit in fruits[:index] + fruits[index+1:]:
        print(f"{fruit} exists elsewhere: True")
    else:
        print(f"{fruit} exists elsewhere: False")

# OUTPUT
# apple exists elsewhere: True
# banana exists elsewhere: False
# apple exists elsewhere: True
# mango exists elsewhere: False
