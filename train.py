

def get_data():
    f = open('inputs-txt/training_data.txt', 'r')
    data = f.readlines()
    data = [[int(i) for i in j.rstrip().split(',')] for j in data]
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    return [x, y]

def calc_error(route1, route2):
    error = 0
    for pos, i in enumerate(route1):
        error += ((i[0] - route2[pos][0]) ** 2 + (i[1] - route2[pos][1]) ** 2) ** 0.5
    return error

