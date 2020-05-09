import datetime

def MySimpleMiddleware(get_response):
    def middleware(request):
        response = get_response(request)
        print("I am simple middleware")
        print("Ip Address: %s" % request.META['REMOTE_ADDR'])
        print("path: %s" % request.path_info)
        print("method: %s" % request.method)
        print("Browser: %s" %request.META['HTTP_USER_AGENT'])
        print("Access Date %s" % datetime.datetime.now())
        return response
    return middleware