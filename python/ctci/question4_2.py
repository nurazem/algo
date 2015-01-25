from Queue import deque

class State:
  UNVISITED = 0
  VISITED = 1
  VISITING = 2

class DirectedGraph:
  def __init__(self,content):
    self.content = content
    self.neighbors = []

def is_route_between(node1, node2):
  if node1 is node2:
    return True
  elif node1 is None or node2 is None:
    return False

  visited = set([node1, node2])
  queue = deque([node1])
  while len(queue) > 0:
    node = queue.popleft()
    for child in node.neighbors:
      if child is node2:
        return True
      elif child not in visited:
        visited.add(child)
        queue.append(child)

  return False

n1 = DirectedGraph(1)
n2 = DirectedGraph(2)
n3 = DirectedGraph(3)
n4 = DirectedGraph(4)
n5 = DirectedGraph(5)
n6 = DirectedGraph(6)

n1.neighbors.append(n2)
n2.neighbors.append(n3)
n2.neighbors.append(n4)
n4.neighbors.append(n5)
n4.neighbors.append(n1)


if is_route_between(n1,n5):
    print "Test 1 passed"

if not is_route_between(n5,n1):
    print "Test 2 passed"

if not is_route_between(n1,n6):
    print "Test 3 passed"





