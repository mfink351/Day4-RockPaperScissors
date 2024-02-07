line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

col = position[0]
colIndex = 0 if col.upper() == "A" else (1 if col.upper() == "B" else 2)
rowIndex = int(position[1]) - 1

map[rowIndex][colIndex] = "X"

print(f"{map[0]}\n{map[1]}\n{map[2]}")