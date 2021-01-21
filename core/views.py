from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from core.maze import Maze


@api_view(['POST'])
@csrf_exempt
def bfs_view(request):
    """Handle bfs request"""

    data = JSONParser().parse(request)
    start_block = tuple(data['start'].values())
    end_block = tuple(data['end'].values())
    walls = data['walls']
    filled_blocks = []
    for row in walls:
        filled_blocks.extend([tuple([x['x'], x['y']]) for x in row])

    path, visited = Maze(start_block, end_block,
                         filled_blocks).bfs_search()

    path = [{'x': pos[0], 'y': pos[1]} for pos in path]
    return JsonResponse({'path': path, 'visited': visited, 'cost': len(path) - 1}, safe=False)


@api_view(['POST'])
@csrf_exempt
def ids_view(request):
    """Handle IDS request"""

    data = JSONParser().parse(request)
    start_block = tuple(data['start'].values())
    end_block = tuple(data['end'].values())
    walls = data['walls']
    filled_blocks = []
    for row in walls:
        filled_blocks.extend([tuple([x['x'], x['y']]) for x in row])

    path, visited = Maze(start_block, end_block,
                         filled_blocks).ids_search()

    path = [{'x': pos[0], 'y': pos[1]} for pos in path]

    return JsonResponse({'path': path, 'visited': visited, 'cost': len(path) - 1}, safe=False)
