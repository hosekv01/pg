def levensteinova_vzdalenost(query1, query2):
    if len(query1) == 0:
        return len(query2)
    if len(query2) == 0:
        return len(query1)
    if query1[-1] == query2[-1]:
        cost = 0
    else:
        cost = 1
    return min(
        levensteinova_vzdalenost(query1[:-1], query2) + 1,
        levensteinova_vzdalenost(query1, query2[:-1]) + 1,
        levensteinova_vzdalenost(query1[:-1], query2[:-1]) + cost
    )

def levensteinova_vzdalenost_for(query1, query2):
    levensteinova_vzdalenost = [[0 for j in range(len(query2) + 1)] for i in range(len(query1) + 1)]
    for i in range(len(query1) + 1):
        levensteinova_vzdalenost[i][0] = i
    for j in range(len(query2) + 1):
        levensteinova_vzdalenost[0][j] = j
    for i in range(1, len(query1) + 1):
        for j in range(1, len(query2) + 1):
            if query1[i - 1] == query2[j - 1]:
                cost = 0
            else:
                cost = 1
            levensteinova_vzdalenost[i][j] = min(
                levensteinova_vzdalenost[i - 1][j] + 1,
                levensteinova_vzdalenost[i][j - 1] + 1,
                levensteinova_vzdalenost[i - 1][j - 1] + cost
            )
    return levensteinova_vzdalenost[len(query1)][len(query2)]
    if len(query1) == 0:
        return len(query2)
    if len(query2) == 0:
        return len(query1)
    if query1[-1] == query2[-1]:
        cost = 0
    else:
        cost = 1


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"
    query4 = "seznam"

    print("Mezi názvy", query1, "a", query2, "je Levensteinova vzdálenost:", levensteinova_vzdalenost_for(query1, query2))
    print("Mezi názvy", query2, "a", query3, "je Levensteinova vzdálenost:", levensteinova_vzdalenost_for(query2, query3))
    print("Mezi názvy", query1, "a", query3, "je Levensteinova vzdálenost:", levensteinova_vzdalenost_for(query1, query3))
    print("Mezi názvy", query1, "a", query4, "je Levensteinova vzdálenost:", levensteinova_vzdalenost_for(query1, query4))

    print("Mezi názvy", query1, "a", query2, "je Levensteinova vzdálenost:", levensteinova_vzdalenost(query1, query2))
    print("Mezi názvy", query2, "a", query3, "je Levensteinova vzdálenost:", levensteinova_vzdalenost(query2, query3))
    print("Mezi názvy", query1, "a", query3, "je Levensteinova vzdálenost:", levensteinova_vzdalenost(query1, query3))
    print("Mezi názvy", query1, "a", query4, "je Levensteinova vzdálenost:", levensteinova_vzdalenost(query1, query4))