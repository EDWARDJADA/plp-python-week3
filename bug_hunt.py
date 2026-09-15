count = 1
total = 0

# BUG: The while statement was missing a colon, so I added one.
# BUG: The loop stopped before adding 5, so I changed < 5 to <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: I could not join a string directly with the integer total, so I used an f-string.
print(f"Sum of 1 to 5 is: {total}")