
def Counter(place): 
    #Creates a list of empty socks to organize
    socks = []

    #Validates if the place being searched for has socks
    #If you have a list, if you don't return it that you don't have socks in place
    if place != "":
        for sock in place:
            socks.append(sock)
    else:
        return "There are no socks in this place Joseph!"

    #Organize the sock list and create a sock filter
    socks = sorted(socks)
    socks_filter = set(socks)

    #Pair counter
    counter = 0

    #Count how many pairs of socks you have, removing those that are missing a pair.
    for sock in socks_filter:
        if (socks.count(sock) % 2) == 0:
            counter += (socks.count(sock) // 2)
        elif (socks.count(sock) // 2) >= 1:
            counter += (socks.count(sock) // 2)

    #Returns how many pairs of socks you have
    return 'Joseph tem {} pares de meias!'.format(counter)

if(__name__ == "__main__"):
    Counter()