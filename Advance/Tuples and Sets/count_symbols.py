data = input()
directory = {}
count = 0
for chr in data:
    if chr not in directory:
        directory[chr] = 1
    elif chr in directory:
        directory[chr] += 1

sorted_dict = {key: value for key, value in sorted(directory.items())}

for k, v in sorted_dict.items():
    print(f"{k}: {v} time/s")



