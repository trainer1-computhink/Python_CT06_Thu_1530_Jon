# ==============================
# SET A — while <condition>:
# ==============================

# A1
count = 1
while count <= 5:
    print(count)
    count += 1

# A2
count = 5
while count >= 1:
    print(count)
    count -= 1

# A3
num = 2
while num <= 10:
    print(num)
    num += 2

# A4
total = 0
num = 1
while num <= 4:
    total += num
    num += 1
print(total)

# A5
count = 1
while count <= 3:
    print("Hello!")
    count += 1


# ==============================
# SET B — Bridge (while condition → break)
# ==============================

# B1
count = 1
while count <= 10:
    print(count)
    if count == 3:
        break
    count += 1

# B2
answer = ""
while answer != "ok":
    answer = input("Type ok: ")
    if answer == "ok":
        break

# B3
guess = 0
while guess != 7:
    guess = int(input("Guess the number: "))
    if guess == 7:
        print("Correct!")
        break

# B4
total = 0
while total <= 20:
    total += 2
    if total > 8:
        print(total)
        break

# B5
numbers = [3, 5, 8, 10]
i = 0
while i < len(numbers):
    if numbers[i] == 8:
        print("Found 8")
        break
    i += 1


# ==============================
# SET C — while True + break
# ==============================

# C1
while True:
    password = input("Enter password: ")
    if password == "python123":
        print("Access granted")
        break

# C2
while True:
    choice = input("Type play or quit: ")
    if choice == "quit":
        print("Goodbye!")
        break

# C3
while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        print("Thank you!")
        break

# C4
import random
while True:
    roll = random.randint(1, 6)
    print("Rolled:", roll)
    if roll == 6:
        break

# C5
while True:
    word = input("Type something: ")
    if word == "stop":
        print("Loop ended")
        break
