

class AirportGraph():
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, airports):
        for airport in airports:
            self._adjacency_list.update({airport: []})
            self._airports = airports

    def add_edge(self, routes):
        for pair in routes:
            tmp = self._adjacency_list.get(pair[0])
            tmp += [pair[1]]
            self._adjacency_list.update({pair[0]: tmp})
            tmp = self._adjacency_list.get(pair[1])
            tmp += [pair[0]]
            self._adjacency_list.update({pair[1]: tmp})

    def bfs(self, start):
        queue = [start]
        visited = set()
        visited.add(start)
        while len(queue) > 0:
            # print(queue)
            airport = queue.pop(0)
            destinations = self._adjacency_list.get(airport)
            for destination in destinations:
                if destination == 'BKK':
                    print('Found it!')
                    return
                if destination not in visited:
                    print(destination)
                    visited.add(destination)
                    queue += [destination]

    def dfs(self, start):
        queue = [start]
        visited = set()
        visited.add(start)
        while len(queue) > 0:
            # print(queue)
            airport = queue.pop(0)
            destinations = self._adjacency_list.get(airport)
            i = 0
            for destination in destinations:
                if destination == 'BKK':
                    print('Found it!')
                    return
                if destination not in visited:
                    print(destination)
                    visited.add(destination)
                    queue.insert(i, destination)
                    i += 1


def main():
    airports = 'PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM'.split(' ')
    routes = [
        ['PHX', 'LAX'],
        ['PHX', 'JFK'],
        ['JFK', 'OKC'],
        ['JFK', 'HEL'],
        ['JFK', 'LOS'],
        ['MEX', 'LAX'],
        ['MEX', 'BKK'],
        ['MEX', 'LIM'],
        ['MEX', 'EZE'],
        ['LIM', 'BKK']
    ]
    airport_graph = AirportGraph()
    airport_graph.add_node(airports)
    airport_graph.add_edge(routes)
    print("\n***BFS***")
    airport_graph.bfs('PHX')
    print("\n***DFS***")
    airport_graph.dfs('PHX')


if __name__ == '__main__':
    main()
