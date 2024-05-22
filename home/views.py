from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home_page(request):
    return render(request, 'home.html')


class GetTest(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated():
            return render(request, 'users:logout')
        else:
            return render(request, 'users:login')
