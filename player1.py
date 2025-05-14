def move1(players, loot):
    """
    Spieler 1 bleibt stehen und gibt seine aktuellen Koordinaten zurück,
    oder bewegt sich einen Schritt zum nächstgelegenen Loot (Manhattan-Distanz).
    :param players: Liste der aktuellen Spielerkoordinaten [(r, c), ...]
    :param loot:   Liste der Loot-Koordinaten
    :return:       Tuple (r, c) mit der neuen Position
    """
    # aktuelle Position von Spieler 1
    r, c = players[0]

    # wenn kein Loot mehr da ist, bleibe stehen
    if not loot:
        return r, c

    # finde den nächsten Loot nach Manhattan-Distanz
    distances = [abs(r - lr) + abs(c - lc) for lr, lc in loot]
    lr, lc = loot[distances.index(min(distances))]

    # bewege dich genau einen Schritt in x- oder y-Richtung
    if lr != r:
        r += 1 if lr > r else -1
    elif lc != c:
        c += 1 if lc > c else -1

    return r, c


if __name__ == "__main__":
    # Testaufruf
    players = [(10, 5), (0, 0)]
    loot    = [(2,3), (15,5), (10,7)]
    for _ in range(5):
        pos = move1(players, loot)
        print("Spieler 1 zieht nach", pos)
        players[0] = pos