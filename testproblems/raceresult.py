
def raceResult():
    print("Enter records")
    records = []
    while True:
        line = input()
        if line.lower() == "d":
            break
        try:
            records.append(eval(line))
        except:
            print("invalid")
    score = {1: 10, 2: 6, 3: 4, 4: 3, 5: 2, 6: 1}
    hashmap = {}
    racer = {}
    print(records)
    for i in range(len(records)):
        print(records[i])
        if records[i][0] in hashmap:
            hashmap[ records[i][0] ].append( [records[i][1],  records[i][2]])
        else:
            hashmap[ records[i][0] ] = [[records[i][1],  records[i][2]]]
    print(hashmap)


    for key, value in hashmap.items():
        print(value)
        for i in range(len(value)):
            if value[i][0] in racer:
                racer[value[i][0]] += score.get(value[i][1])
            else:
                racer[value[i][0]] = score.get(value[i][1])
    print(racer)

    sorted_racer = sorted(racer.items(), key=lambda value: value, reverse=True)
    print(sorted_racer)
    for ranking in sorted_racer:
        racer_name, points = ranking[0], ranking[1]
        print(racer_name, points)
    return True  




[2001, 1001, 3]
[2001, 1002, 2]
[2002, 1003, 1]
[2002, 1001, 2]
[2002, 1002, 3]
[2001, 1003, 1]
raceResult()