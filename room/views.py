from django.shortcuts import render
from .models import Room


# rooms = [
##  {'id': 1, 'name':'Lets Code'},
## {'id': 2, 'name':'Lets Code'},
# {'id': 3, 'name':'Lets Code'},
#]
    


# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context={'rooms': rooms}
    return render(request, 'home.html',context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    #for i in rooms:
     #   if i['id'] == int(pk):
            #room = i
    context={'room': room}
    return render(request, 'room.html',context)

def createRoom(request):
    context = {}
    return render(request,'room_form.html',context)