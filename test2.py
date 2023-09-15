import math

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
cutoff = 3

mean = sum(sample)/len(sample)
sd = []


def stand_dev():
    global sample, mean, sd
    for i in sample:
        sd.append((i-mean)**2)
    return math.sqrt(sum(sd)/len(sample))

deviation = stand_dev()
print(deviation)

for i in range(len(sample)):
    if sample[i] > deviation * cutoff:
        sample.remove(sample[i])
print(sample)

mean = sum(sample)/len(sample)
deviation = stand_dev()

print(mean, deviation)