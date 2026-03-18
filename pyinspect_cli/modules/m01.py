def it(s,t):
    rows = len(s) + 1
    cols = len(t) + 1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    for i in range(1, rows):
        dist[i][0] = i

    for j in range(1, cols):
        dist[0][j] = j

    for row in range(1, rows):
        for col in range(1, cols):
            if s[row - 1] == t[col - 1]:
                cost = 0
            else:
                cost = 1

            dist[row][col] = min(
                dist[row - 1][col] + 1,
                dist[row][col - 1] + 1,
                dist[row - 1][col - 1] + cost
            )

    for r in range(rows):
        print(dist[r])
    return dist[rows - 1][cols - 1]


s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")
print("Edit Distance between: ",s1, "and", s2, "is", it(s1, s2))