from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Message, User, Content
from .forms import UserForm, MessageForm
from django.http import HttpResponse
from django.db.models import Avg

# Create your views here.

def createUser(request):
    if request.method == 'POST':
        print('create post')
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('messages:home')
    else:
        print('create get')
        form = UserForm()
    return render(request, 'messages/create-user.html',{'forms': form})


#  TODO: Add this logic where user cannot send msg to himself
def home(request):
    print('request', request)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('messages:home')
        return render(request, 'messages/home.html', {"forms": form})
    else:
        print('not in if')
    users = User.objects.all()
    content = Content.objects.all()
    messages = Message.objects.all()
    context = {'users': users, 'contents': content, 'messages': messages}
    return render(request, 'messages/home.html', context)

def sendMessage(request):
    print('request', request)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('messages:home')
        return render(request, 'messages/home.html', {"forms": form})
    else:
        print('not in if')
    users = User.objects.all()
    content = Content.objects.all()
    messages = Message.objects.all()
    context = {'users': users, 'contents': content, 'messages': messages}
    return render(request, 'messages/send-message.html', context)


def stats(request):
        users = User.objects.all().values()
        zayyan = users.filter(username='zayyan').values()
        content = Content.objects.all()
        messages = Message.objects.all().values()
        result = User.objects.aggregate(Avg('age'))
        print('result', result)
        # print('zayyan', zayyan)
        # print('users', users[0]['username'])
        # for message in messages:
        #     print('message', message)
        zayyan_id = ''
        users_age = {}
        for user in users:
            age = user['age']
            if(age in users_age):
                users_age[age] += 1
            elif(age not in users_age):
                users_age[age] = +1
            if(user['username'] == 'Zayyan'):
                zayyan_id = user['id']
        # how many texts were sent from you to users of each age bracket
        mySent = []
        receivers = []
        message_frequency = {}
        for message in messages:
            print('messageZ', message['content_id'])
            content = message['content_id']
            if(content in message_frequency):
                message_frequency[str(content)] += 1
            elif(content not in message_frequency):
                message_frequency[str(content)] += 1
            if(message['sender_id'] == zayyan_id):
                mySent.append(message)
                print('checkZ', message['receiver_id'])
                receiver = User.objects.all().filter(id=message['receiver_id'])
                print('receiver', receiver)
                receivers.append(receiver)
                
        print('message_frequency', message_frequency)
        print('mySent', mySent)
        print('receivers', receivers)
        # for userZ in receiver:
        #     print('userZ', userZ)
        print('number of users in each age bracket', users_age)
        context = {'users': users, 'contents': content, 'messages': messages}
        
        
        
        return render(request,'messages/stats.html',{"data":context})
