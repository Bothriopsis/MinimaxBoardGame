def move1(players, loot):
    """
    Spieler 1 bleibt stehen und gibt seine aktuellen Koordinaten zurück,
    oder bewegt sich einen Schritt zum nächstgelegenen Loot (Manhattan-Distanz).
    :param players: Liste der aktuellen Spielerkoordinaten [(r, c), ...]
    :param loot:   Liste der Loot-Koordinaten
    :return:       Tuple (r, c) mit der neuen Position
    """
    r, c = players[0]

    if not loot:
        return r, c

    distances = [abs(r - lr) + abs(c - lc) for lr, lc in loot]
    lr, lc = loot[distances.index(min(distances))]

    if lr != r:
        r += 1 if lr > r else -1
    elif lc != c:
        c += 1 if lc > c else -1

    return r, c