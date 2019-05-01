global costs
costs = []


def backtrack(adjmat, order, best_tour, best_tour_cost, partial_tour, partial_tour_cost, level):
    global btc
    btc = best_tour_cost
    print(btc)
    if level == order - 1:
        tour_cost = partial_tour_cost + adjmat[partial_tour[order - 2]][partial_tour[order - 1]] + adjmat[partial_tour[order - 1]][0]
        if btc == 0 or tour_cost < btc:
            costs.append(tour_cost)
            btc = min(costs)
    else:
        for i in range(level, order, 1):
            if btc == 0 or partial_tour_cost + adjmat[partial_tour[level - 1]][partial_tour[i]] < btc:
                partial_tour[level], partial_tour[i] = partial_tour[i], partial_tour[level]
                cost = adjmat[partial_tour[level - 1]][partial_tour[level]]
                partial_tour_cost += cost
                backtrack(adjmat, order, best_tour, btc, partial_tour, partial_tour_cost, level + 1)
                partial_tour_cost -= cost
                partial_tour[level], partial_tour[i] = partial_tour[i], partial_tour[level]

    print(partial_tour)


def tsp_solution(m, order, bt):
    best_tour_cost = 0
    partial_tour_cost = 0
    partial_tour = [0] * order
    if partial_tour is None or bt is None:
        bt = None
        return 0
    for i in range(order):
        partial_tour[i] = i

    backtrack(m, order, bt, best_tour_cost, partial_tour, partial_tour_cost, 1)
    return min(costs)


if __name__ == '__main__':
    graph = [[0, 5, 7, 9, 10],
             [4, 0, 11, 3, 7],
             [3, 1, 0, 4, 5],
             [6, 5, 7, 0, 11],
             [13, 2, 8, 3, 0]]

    size = 5  # vertex
    best_tour = [0] * size
    tsp_cost = tsp_solution(graph, size, best_tour)
    print(tsp_cost)
    print(best_tour)


