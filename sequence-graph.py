reads = ["catgctaattc", "attcgcatgcta"]

graph = {"forwards" : {}, "reverse" : {}}

print(graph)

def add_edge(graph, vertexfrom, vertexto):
  if vertexfrom not in graph['forwards']:
    graph['forwards'][vertexfrom] = [vertexto]
  else:
    graph['forwards'][vertexfrom].append(vertexto)

  if vertexto not in graph['reverse']:
    graph['reverse'][vertexto] = [vertexfrom]
  else:
    graph['reverse'][vertexto].append(vertexfrom)


graph['reverse']['atgc'] = ['catg']

print(graph)

graph = {"forwards" : {}, "reverse" : {}}
add_edge(graph, 1, 2)
add_edge(graph, 1, 3)
print(graph)
