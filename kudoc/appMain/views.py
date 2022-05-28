from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from appAccount.models import *
# Create your views here.
def index(request):
    # print(request.user.email)
    # toyo30@naver.com 가 출력된다. 
    # 현재 로그인되어있는 유저를 말한다. 
    # template 에서는 {{user}}로 출력할 수 있다.
    # 로그인 안 된 상태에서 request.user는 anonymousUser를 출력하게 된다.
    # print(request.user.email)

    # 로그인이 되어있는지 안 되어있는지에 대한 속성은 
    #is_authenticated 를 사용한다.
    # request.user.is_authenticated
    # 로그인되어 있으면, true
    # 로그인 안 되어있으면, false를 출력
    # true or false로 판별됨
    notices = Notice.objects.all()


    return render(request, "appMain/index.html", {"notices":notices,}
    )


def profile(request):
    return render(request, "appMain/profile.html")


def profileEdit(request):
    return render(request, "appMain/profileEdit.html")


def notice(request):
    return render(request, "appMain/notice.html")

def noticeDetail(request):
    return render(request, "appMain/noticeDetail.html")