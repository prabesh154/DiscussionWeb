from django.shortcuts import render



rooms = [
    {'id': 1, 'name':'Lets Code'},
    {'id': 2, 'name':'Lets Code'},
    {'id': 3, 'name':'Lets Code'},
]
    


# Create your views here.
def home(request):
    context={'rooms': rooms}
    return render(request, 'home.html',context)


def room(request,pk):
    return render(request, 'room.html')