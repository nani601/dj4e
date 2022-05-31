from django.shortcuts import render, redirect, reverse
from django.views import View
from django.conf import settings
# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class HomeView(View):
    def get(self, request):
        print(request.get_host())
        strval = request.GET.get("search", False)
        if strval != False:
            # ?query parameter 不能在urls.py中进行匹配
            print("find search, pass to ads deal")
            # return redirect(reverse('ads:all', kwargs={"search": strval}))
            # print(reverse('ads:all')+'?search=' + strval)
            # return redirect(reverse('ads:all')+'?search=' + strval)
            # https://stackoverflow.com/questions/4808329/can-i-call-a-view-from-within-another-view
            from ads.views import AdListView
            return AdListView.as_view()(request)
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'home/main.html', context)
