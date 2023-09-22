import copy

def teamwork_climb(elevations, path, ponies):
    '''will return a dictionary simulating the movement of selfish and
    altruistic pony with key = timestamp and value = pony information'''

    ts = 0
    result_og = {ts: ponies}

    return teamwork_segment(elevations, path, ponies, ts, result_og)


def teamwork_segment(elevations, path, ponies, ts, result_og):
    '''will return a new item in the dictionary which contains
    information on the ponies for the next timestamp'''

    num_ponies_unavailable = 0
    # ponies are unavailable if they do not have enough energy, or have
    # arrived to the final destination, and have considered at least one move

    result = copy.deepcopy(result_og)

    current_ts = []
    # will contain info on ponies corresponding to the new ts in the dictionary

    for pony in result[ts]:

        p_id = pony[0]
        p_type = pony[1]
        p_energy = pony[2][0]
        p_location = pony[2][1]

        if p_type == "a":
            for other_pony in result[ts][0:p_id]:  # Comparing the "a" pony with other ponies with a smaller id
                if other_pony[2][1] == p_location:  # Checks if other pony are at same location
                    # print(other_pony)
                    # Now check out of these other ponies, which do not have enough energy to move to next location
                    # energy required is = to the elevation change, e.g. 5 energy needed = 5 elevation increase
                    i = path.index(other_pony[2][1])  # gets the index of the current location for the other ponies
                    current_elevation = elevations[path[i][0]][path[i][1]]
                    # print(current_elevation)
                    next_elevation = elevations[path[i + 1][0]][path[i + 1][1]]
                    # print(next_elevation)
                    elevation_change = next_elevation - current_elevation
                    # print(elevation_change)
                    if other_pony[2][0] < elevation_change:
                        # the other pony's energy is less than the energy required to get to next step
                        energy_needed = elevation_change - other_pony[2][0]
                        # print(energy_needed)
                        # print(other_pony)
                        # Now need to update the new energies of the other ponies and "a" pony
                        # First subtract energy from "a" then add onto the other pony until "a" can no longer give
                        pony[2][0] -= energy_needed
                        if pony[2][0] < 0:  # if "a" energy is negative then can no longer add energy onto other ponies
                            break
                        else:
                            other_pony[2][0] += energy_needed
                            current_ts.append(other_pony)
                        # after updating energies, "a" will move if it has enough energy while other ponies stay still
                        if pony[2][0] >= elevation_change:
                            pony[2][0] -= elevation_change  # updates the new energy of "a" pony
                            pony[2][1] = path[path.index(pony[2][1]) + 1]  # updates the new position of "a" pony
                    else:
                        # the other ponies have enough energy so don't need extra, so just update new energy & position
                        print("dont need energy")
            current_ts.append(pony)
            # ts_original[1] = current_ts
            # print(ts_original)
            result_og[ts + 1] = current_ts
            print(result_og)

    # return teamwork_segment(elevations, path, ponies, ts + 1, result)      # recursion, will continue to find the next
    # timestamp (ts + 1) and info until no more ponies are available


teamwork_climb([[0, 10, 5], [0, 0, 10]], [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 's', [2, (0, 0)]), (1, 's', [6, (0, 0)]), (2, 'a', [2, (0, 0)])])