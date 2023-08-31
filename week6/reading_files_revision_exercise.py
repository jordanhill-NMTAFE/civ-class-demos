# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0.0
iterations = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    iterations += 1
    count = float(line.split(":")[1].strip()) + count
print(iterations)
print(count)
print(count/iterations)
fh.close()
print("Done")
