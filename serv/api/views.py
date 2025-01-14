from datetime import datetime
import json

from django.http import JsonResponse


def d_time(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        d = datetime.now()
        r = json.dumps({'date': str(d.date()), 'time': str(d.time())})

        return JsonResponse(r, safe=False)
