from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, "home.html")

def room(request, room):
    username = request.GET.get('username')
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        return redirect('/')
    return render(request, "room.html", {"username": username, "room_details": room_details, "room": room})

def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room_name).exists():
        return redirect('/' + room_name + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        return redirect('/' + room_name + '/?username=' + username)

def send(request):
    message = request.POST["message"]
    username = request.POST["username"]
    room_id = request.POST["room_id"]
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        return HttpResponse('Room does not exist', status=404)

    new_message = Message.objects.create(value=message, user=username, room=room)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    try:
        room_details = Room.objects.get(name=room)
        messages = Message.objects.filter(room=room_details).values('user', 'value', 'date')
        return JsonResponse({"messages": list(messages)})
    except Room.DoesNotExist:
        return JsonResponse({"messages": []}, status=404)
