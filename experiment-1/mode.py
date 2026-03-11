d = {}
n = int(input("Enter how many data to be entered: "))

for o in range(n):
    x = int(input("Enter number: "))
    d[x] = d.get(x, 0) + 1

max_freq = max(d.values())
modes = [k for k, v in d.items() if v == max_freq]

if max_freq == 1:
    print("No mode")
elif len(modes) == 1:
    print("Mode is", modes[0])
else:
    print("Modes are", modes)
