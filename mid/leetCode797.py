#797. All Paths From Source to Target
# [(0, [0])]
# [(1, [0, 1]), (2, [0, 2])]
# [(2, [0, 2]), (3, [0, 1, 3])]
# [(3, [0, 1, 3]), (3, [0, 2, 3])]
# [(3, [0, 2, 3])]

def allPathsSourceTarget(graph):
      result, target = [], len(graph) - 1
      curPath = [[0]]

      while curPath:
          path = curPath.pop(0)
          if path and len(path) != 0:
              lastNode = path[-1]
              if lastNode == target:
                  result.append(path)
              for val in graph[lastNode]:
                  curPath.append(path + [val])

      print(result)

graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]
allPathsSourceTarget(graph)

