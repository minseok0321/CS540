import copy

def fill(state, max, which):
    copy = state.copy()
    copy[which] = max[which]
    return copy

def empty(state, max, which):
    copy = state.copy()
    copy[which] = 0
    return copy
    
def xfer(state, max, source, dest):
    copy = state.copy()
    copy[dest] += copy[source]
    if copy[dest] > max[dest]:
        copy[source] = copy[dest] - max[dest]
        copy[dest] = max[dest]
    else:
        copy[source] = 0
        
    return copy
    
def succ(state, max):
    output = []
    output.append(fill(state, max, 0))
    output.append(fill(state, max, 1))
    output.append(empty(state, max, 0))
    output.append(empty(state, max, 1))
    output.append(xfer(state, max, 1, 0))
    output.append(xfer(state, max, 0, 1))
    
    for i in output:
        print(i)
    
