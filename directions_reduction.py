def dirReduc(arr):
    d_dict = {
        "NORTH":"SOUTH",
        "SOUTH":"NORTH",
        "EAST":"WEST",
        "WEST":"EAST"
    }
    
    x = arr
    same = False
    while same == False:
        m = []
        y = []
        for d in range(1, len(x)):
            if d_dict[x[d]] == x[d-1]:
                if d-1 not in y:
                    y += [d, d-1]

        for d in range(0, len(x)):
            if d not in y:
                m.append(x[d])
        if x == m:
            return m
        else:
            x = m


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
#  ['WEST'])
u = ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u))
#  ["NORTH", "WEST", "SOUTH", "EAST"])
z = ['NORTH', 'EAST', 'EAST', 'NORTH', 'NORTH',
     'NORTH', 'SOUTH', 'NORTH', 'EAST', 'WEST', 'SOUTH']
print(dirReduc(z))
# ['NORTH', 'EAST', 'EAST', 'NORTH', 'NORTH']
