populations = [1000, 2000, 3000, 4000, 5000, 6000, 2000]

print(populations)

print(populations[-1])

print(type(populations[-1]))

print(populations[0])

print(populations[1])

print(populations[-2])
print(populations[4])

populations.append(7000)
print(populations)

populations.insert(3, 3500)
print(populations)

populations = list(filter((2000).__ne__, populations))
print(populations)

print(test2)