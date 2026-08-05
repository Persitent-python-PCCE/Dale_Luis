goblin = ["Queens","Manhattan","Brooklyn","Bronx"]
octopus = ["Manhattan","Brooklyn","Harlem"]
vulture = ["Manhattan","Bronx","Harlem"]

def common_place(*args):
    g=set(args[0])
    o=set(args[1])
    v=set(args[2])
    
    common= g & o & v
    return common
    
def one_place(*args):
    g=set(args[0])
    o=set(args[1])
    v=set(args[2])
    
    one= (g - o - v)|(o - g - v)|(v - g - o)
    return one

def hoods(*args):
    g=set(args[0])
    o=set(args[1])
    v=set(args[2])
    
    total = len(g|o|v)
    return total

print("Contested by all three: ",common_place(goblin,octopus,vulture))

print("Controlled by exactly one: ",one_place(goblin,octopus,vulture))

print("Distinct neighborhoods: ",hoods(goblin,octopus,vulture))