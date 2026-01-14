#ЗАПРАВКА
def min_refuels(distances, S):
    n = len(distances)
    fuel = S
    stops = 0
    for i in range(n):
        if distances[i] > S:
            return -1  # невозможно проехать
        if fuel < distances[i]:
            stops += 1
            fuel = S
        fuel -= distances[i]
    return stops

#ЭСКУРСИЯ
def max_excursions(intervals):
    intervals.sort(key=lambda x: x[1])  # сортировка по окончанию
    selected = []
    last_end = -1
    for a, b in intervals:
        if a >= last_end:
            selected.append((a, b))
            last_end = b
    return selected