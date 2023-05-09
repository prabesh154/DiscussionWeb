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
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context={'room': room}
    return render(request, 'room.html',context)