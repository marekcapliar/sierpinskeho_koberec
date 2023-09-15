def josephus_survivor(n,k):
    people = [i for i in range(1, n+1)]
    delete = k-1
    while len(people) > 1:
        while delete >= len(people):
            delete -= len(people)
        people.remove(people[delete])
        delete += k-1
    return people[0]


print(josephus_survivor(7, 3))