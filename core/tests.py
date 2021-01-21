import json

from rest_framework.test import APIClient, APITestCase


class MazeTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.data = {"start": {"x": 3, "y": 0}, "end": {"x": 0, "y": 3},
                     "walls": [[{"x": 0, "y": 0}], [{"x": 1, "y": 2}], [{"x": 2, "y": 0}], [{"x": 3, "y": 3}]]}

    def test_bfs(self):
        """Test BFS Algorithm"""

        response = self.client.post(
            'http://127.0.0.1:8000/api/bfs/', self.data, format='json')

        res_data = json.loads(response.content)
        path = [tuple(x.values()) for x in res_data['path']]
        visited = [tuple(x.values()) for x in res_data['visited']]

        e_path = [(3, 0), (3, 1), (2, 1), (1, 1),
                  (0, 1), (0, 2), (0, 3)]
        e_visited = [(3, 0), (3, 1), (2, 1), (3, 2), (1, 1), (2, 2),
                     (0, 1), (1, 0), (2, 3), (0, 2), (1, 3), (0, 3)]

        self.assertEqual(path, e_path)
        self.assertEqual(visited, e_visited)

    def test_ids(self):
        """Test IDS"""

        response = self.client.post(
            'http://127.0.0.1:8000/api/ids/', self.data, format='json')

        res_data = json.loads(response.content)
        path = [tuple(x) for x in res_data[0]]
        visited = dict()
        for i in res_data[1]:
            visited[i] = [tuple(x) for x in res_data[1][i]]

        e_path = [(3, 0), (3, 1), (2, 1), (1, 1),
                  (0, 1), (0, 2), (0, 3)]
        e_visited = {
            '0': [{'x': 3, 'y': 0}],
            '1': [{'x': 3, 'y': 0}, {'x': 4, 'y': 0}, {'x': 3, 'y': 1}],
            '2': [{'x': 3, 'y': 0}, {'x': 4, 'y': 0}, {'x': 5, 'y': 0}, {'x': 4, 'y': 1}, {'x': 3, 'y': 1}, {'x': 2, 'y': 1}, {'x': 3, 'y': 2}],
            '3': [{'x': 3, 'y': 0}, {'x': 4, 'y': 0}, {'x': 5, 'y': 0}, {'x': 6, 'y': 0}, {'x': 5, 'y': 1}, {'x': 4, 'y': 1}, {'x': 3, 'y': 1}, {'x': 4, 'y': 2}],
            '4': [{'x': 3, 'y': 0}, {'x': 4, 'y': 0}, {'x': 5, 'y': 0}, {'x': 6, 'y': 0}, {'x': 7, 'y': 0}, {'x': 6, 'y': 1}, {'x': 5, 'y': 1}, {'x': 4, 'y': 1}, {'x': 5, 'y': 2}, {'x': 3, 'y': 1}, {'x': 2, 'y': 1}, {'x': 1, 'y': 1}, {'x': 0, 'y': 1}, {'x': 1, 'y': 0}, {'x': 2, 'y': 2}],
            '5': [{'x': 3, 'y': 0}, {'x': 4, 'y': 0}, {'x': 5, 'y': 0}, {'x': 6, 'y': 0}, {'x': 7, 'y': 0}, {'x': 8, 'y': 0}, {'x': 7, 'y': 1}, {'x': 6, 'y': 1}, {'x': 5, 'y': 1}, {'x': 6, 'y': 2}, {'x': 4, 'y': 1}, {'x': 3, 'y': 1}, {'x': 2, 'y': 1}, {'x': 1, 'y': 1}, {'x': 2, 'y': 2}, {'x': 3, 'y': 2}, {'x': 4, 'y': 2}],
            '6': [(3, 0), (3, 1), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3)],
        }

        self.assertEqual(path, e_path)
        self.assertEqual(visited, e_visited)

    def test_a_star(self):
        """Test A*"""

        response = self.client.post(
            'http://127.0.0.1:8000/api/astar/', self.data, format='json')

        res_data = json.loads(response.content)
        path = [tuple(x) for x in res_data[0]]
        visited = [tuple(x) for x in res_data[1]]

        e_path = [(3, 0), (3, 1), (2, 1), (1, 1),
                  (0, 1), (0, 2), (0, 3)]
        e_visited = [(3, 0), (3, 1), (2, 1), (3, 2), (1, 1), (2, 2),
                     (0, 1), (1, 0), (2, 3), (0, 2), (1, 3), (0, 3)]

        self.assertEqual(path, e_path)
        self.assertEqual(visited, e_visited)
