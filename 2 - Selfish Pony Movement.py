def selfish_climb(elevations, path, ponies):
    '''will return a dictionary of the movement of selfish ponies'''

    ts = 0  # initial timestamp
    result = {ts: ponies}  # starting position of ponies

    return selfish_step(ts, path, elevations, result, ponies)


def selfish_step(ts, path, elevations, result, ponies):
    '''will return a new item in the dictionary which contains 
    information on the ponies for the next timestamp'''

    num_ponies_unavailable = 0
    # ponies are unavailable if they do not have enough energy, or have
    # arrived to the final destination, and have considered at least one move

    current_tp = []
    # will contain info on ponies corresponding to the new ts in the dictionary

    for pony in result[ts]:
        # accessing each pony info in the value of the dictionary

        if pony[0] <= ts:
            # if the pony id is <= timestamp, then it is available to move
            if pony[2][1] != path[-1]:
                # if the position/coord of pony != final path cell, then 
                # find the current elevation corresponding to the current 
                # position as well as elevation of next cell
                i = path.index(pony[2][1])
                successive_elevation = (elevations[path[i + 1][0]][path[i + 1][1]])
                former_elevation = elevations[path[i][0]][path[i][1]]
                relative_elevation = successive_elevation - former_elevation
                # calculates the elevation change, will be used to find
                # energy change

                if pony[2][0] >= relative_elevation:
                    # if the current energy is >= elevation change, then find
                    # new energy (energy) and new position (current)
                    pony = list(pony)
                    energy = pony[2][0] - relative_elevation
                    current = path[path.index(pony[2][1]) + 1]
                    pony[2] = [energy, current]
                    # replace the old energy and position with new info
                    pony = tuple(pony)
                    current_tp.append(pony)

                else:
                    # if the current energy is too low, then info is unchanged
                    # and increase the num of unavailable ponies
                    current_tp.append(pony)
                    num_ponies_unavailable += 1
                    if len(ponies) == num_ponies_unavailable:
                        # if the num of ponies = num of unavailable ponies
                        # then check whether all ponies have considered a move
                        if len(result) == len(ponies):
                            # if the number of dict items = num of ponies, then
                            # must add same dictionary item in order to
                            # ensure all ponies have considered a move
                            result[ts + 1] = current_tp
                            return result
                        else:
                            return result
            else:
                # position of pony is equal to final cell, so append old info
                # and increase num of unavailable ponies
                current_tp.append(pony)
                num_ponies_unavailable += 1
                if len(ponies) == num_ponies_unavailable:
                    # return the result/dictionary if the number of ponies =
                    # number of unavailable ponies
                    return result
        else:
            # pony id is not <= ts, so cannot move, information is unchanged
            current_tp.append(pony)

    result[ts + 1] = current_tp
    # adds new dictionary item with key=next timestamp, value=new ponies info

    # recursion, will continue to find the next timestamp (ts + 1) and info until no more ponies are available
    return selfish_step(ts + 1, path, elevations, result, ponies)
