from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from chats.main_model import rps

def main(request):
    return render(request,'chats/index.html')

def get_message(request):
    message = request.GET.get('message', None)
    print(message)
    rp = rps(message)
    rep = f"""<div class="d-flex flex-row p-3"> <img src="/static/bot.png" width="30" height="30">
            <div class="chat ml-2 p-3">{rp}</div>
        </div>"""
    echo = f"""<div class="d-flex flex-row p-3"> <img src="https://img.icons8.com/color/48/000000/circled-user-male-skin-type-7.png" width="30" height="30">
            <div class="chat ml-2 p-3">{message}</div>
        </div>"""
    reponse = {
        "rep":rep,
        "echo":echo,
    }
    return JsonResponse(reponse)