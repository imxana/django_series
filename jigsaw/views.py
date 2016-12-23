from django.shortcuts import render
from django.http import HttpResponse

import json

# Create your views here.

def api_test(request):
    msg = { 
        'METHOD'   : request.method, 
        'BODY'     : request.body.decode(),
        'GET_DATA' : request.GET,
        'POST_DATA': request.POST,
        'META'     : {},
    }
    for k,v in request.META.items():
        # msg['META'][k] = str(v)
        if k.startswith('HTTP_') or k.startswith('CONTENT_'):
            msg['META'][k] = v

    # jsonify
    smsg = json.dumps(msg, indent=1) 

    # set the font red
    print("\033[31mapi test ok.\n%s\033[00m"%smsg)

    return HttpResponse(smsg)



def image_callback(request):
    '''
    callbackBody: filename should be unique
    callbakUrl: ./api/image/callback
    '''
    # if request.method != 'POST':
        # return json.dumps({'code':'0'})
    fname = request.POST.get('filename','') 
    if fname == '':
        return HttpResponse(json.dumps({'code':'0'}))
    url = 'https://oi3qt7c8d.qnssl.com/' + fname
    return HttpResponse(json.dumps({'code':'1','url':url}))



def image_query(request):
    return HttpResponse('')



