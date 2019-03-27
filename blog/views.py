from django.shortcuts import render

# Create your views here.
def post_list(request):#esto es una funcion que la llamamoms como le colocamos en las url de la app
    return render(request, 'blog/post_list.html', {})