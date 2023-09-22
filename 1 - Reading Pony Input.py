def read_ponies(filename):
    file1 = open(filename)
    lst = [line.strip() for line in file1]
    elevations = []
    path = []
    ponies = []
    ans = []

    for i in range(len(lst)):

        if lst[i] == 'Elevations:':
            for j in lst[i + 1:]:
                if j == '':
                    break
                elevations.append(j)

        if lst[i] == 'Path:':
            for j in lst[i + 1:]:
                if j == '':
                    break
                path.append(j)

        if lst[i] == 'Ponies:':
            for j in lst[i + 1:]:
                if j == '':
                    break
                ponies.append(j)

    for elv in range(len(elevations)):
        elevations[elv] = list(eval(elevations[elv]))
    ans.append(elevations)

    for cell in range(len(path)):
        path[cell] = eval(path[cell])
    ans.append(path)

    ponies1 = []
    for pony in ponies:
        a = [i for i in pony if (i != "," and i != " ")]

        num = int(a.pop(0))
        letter = a.pop(0)
        energy = ""
        loc = []

        for i in a[1: a.index("(")]:
            energy += i

        energy = int(energy)

        for i in a[a.index("(") + 1:a.index(")")]:
            loc.append(int(i))

        loc = tuple(loc)

        info = (num, letter, [energy, loc])

        ponies1.append(info)

    ans.append(ponies1)

    return tuple(ans)

