def move1(players, loot):
    
    """
    Spieler 1 bleibt stehen und gibt seine aktuellen Koordinaten zurück.
    :param players: Liste der aktuellen Spielerkoordinaten [(r, c), ...]
    :param loot: Liste der Loot-Koordinaten (wird hier nicht verwendet)
    :return: Tuple (r, c) mit der neuen Position (gleich altem Wert)
    """
    # players[0] entspricht den Koordinaten von Spieler1
    if players[0][0] >= 0 and players[0][1] >= 0:
        return tuple(players[0][0], players[0][1] + 1)
    else:
        return tuple(players[0][0], players[0][1] - 1)