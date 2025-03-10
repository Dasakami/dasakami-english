from django.shortcuts import render , redirect

def home(request):
    return render(request , 'main/home.html')

def app(request):
    return render(request, 'main/app.html' )



def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)

def permission_denied(request, exception):
    return render(request, '403.html', status=403)


def open_admin(request):
    return redirect('admin:index')  

# Create your views here.
