from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
def index(request):
    view_cnt = request.session.get("view_cnt", 0) + 1
    request.session["view_cnt"] = view_cnt
    if view_cnt >= 5:
        del request.session["view_cnt"]
    resp = HttpResponse("view count={}".format(view_cnt))
    if not request.COOKIES.get("dj4e_cookie"):
        resp.set_cookie('dj4e_cookie', 'a398c375', max_age=1000)
    return resp