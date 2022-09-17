# chat/views.py
from django.shortcuts import render
from app01.consumers import phone_set


def index(request):
    tel = request.GET.get('tel')
    pk = request.GET.get('id')
    if tel:
        return render(request, "index.html", {"tel": tel, "id": pk})
    else:
        return render(request, "check_Phone.html")


def chat_home(request):
    # user_obj = UserInfo.objects.all()
    print(phone_set)
    return render(request, "home.html", {"user_obj": phone_set})
