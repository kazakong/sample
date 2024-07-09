n = int(input())
yesterday = input()
today = input()

ocuppied = 0

for i in range(len(yesterday)):
    if yesterday[i] == "C" and today[i] == "C":
        ocuppied += 1

print(ocuppied)