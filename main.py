
def _min(file_name):
    data = sorted([int(i) for i in open(file_name, 'r').read().split(' ')])
    return data[0]
def _max(file_name):
    data = sorted([int(i) for i in open(file_name, 'r').read().split(' ')])
    return data[-1]
def _sum(file_name):
    data = sorted([int(i) for i in open(file_name, 'r').read().split(' ')])
    return sum(data)
def _mult(file_name):
    data = sorted([int(i) for i in open(file_name, 'r').read().split(' ')])
    a = 1
    for i in data:
        a*=i
    return a

