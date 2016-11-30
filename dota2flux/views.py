from django.http import HttpResponse
import dota2api
import json
api = dota2api.Initialise("F2BE28B872743FD96ACD3F841E81A938")


def index(request):
    hist = api.get_match_history(account_id=105885624)

    return HttpResponse(hist.json)



'''
def index(request):
    hist = api.get_match_history(account_id=105885624)

    return HttpResponse(hist.json)
'''

'''

import json

def index(request):
    hist = api.get_match_history(account_id=105885624)
    json_parsed = json.loads(hist.json)

    return HttpResponse(json_parsed['season'])

------------------------

def index(request):
    hist = api.get_match_history(account_id=105885624)
    json_parsed = json.loads(hist.json)

    return HttpResponse(json_parsed['matches'][0]['players'][0]['account_id'])

'''