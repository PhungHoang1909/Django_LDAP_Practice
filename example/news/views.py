from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
import requests

class HomeView(View):
    @method_decorator(login_required)
    def get(self, request):
        api_key = 'eb39576156744e22addb8a389e485666'
        url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + api_key
        response = requests.get(url)
        news_data = response.json()
        return render(request, 'home.html', {'news_data': news_data})
