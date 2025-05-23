from collections import defaultdict

def isvalid(graph, var, color, ass):
    for key in graph[var]:
        if ass[key] == color:
            return False
    return True

def csp(graph, colors):
    vars = list(graph.keys())
    ass = defaultdict(str)
    for var in vars:
        for color in colors:
            if isvalid(graph, var, color, ass):
                ass[var] = color
                break
        else:
            return "Not Possible"
    return dict(ass)  # Convert to regular dict

result = csp(graph={
    'WA': ['NT'],
    'NT': ['WA', 'SA', 'QLD'],
    'SA': ['WA', 'NT', 'QLD', 'VIC'],
    'QLD': ['NT', 'SA', 'NSW'],
    'NSW': ['QLD', 'SA', 'VIC'],
    'VIC': ['SA', 'NSW'],
    'TAS': []
}, colors=['red', 'green', 'blue', 'yellow'])

print(result)
