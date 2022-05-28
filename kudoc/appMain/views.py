from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from appAccount.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
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


@login_required(login_url="/login")
def profile(request):
    return render(request, "appMain/profile.html")


def profileEdit(request):
    categorys = Category_Item.objects.all()
    email_periods = Email_period.objects.all()
    print(categorys)
    print(email_periods)
    if request.method == 'POST':
        print(request.user)
        print(request)
        print(request.user.id)
        print(User.objects.get(id=request.user.id))
        user = User.objects.get(id=request.user.id)
        user.email = request.POST['email'],
        user.nickname = request.POST['nickname'],
        # user.phone_number = request.POST['phone_number'],
        # user.email_period = Email_period.objects.get(period=request.POST['email_period']),
        # user.category = Category_Item.objects.get(pk=1),
        
        user.save()
        # user.objects.update(
        #     department = request.POST['department'],
        #     nickname = request.POST['nickname'],
        #     email = request.POST['email'],
        #     phone_number = request.POST['phone_number'],
        #     # category = Category_Item.objects.get(pk=1)
        #     # email_period = Email_period.objects.get(pk=1),
        #     is_actice = True,
        #     is_premier = True,
        # )
        return redirect('index')
    return render(request, "appMain/profileEdit.html", {
        'categorys':categorys,
        'email_periods':email_periods,
    })


def notice(request):
    return render(request, "appMain/notice.html")

def noticeDetail(request):
    return render(request, "appMain/noticeDetail.html")

'''
class User(AbstractUser):
    #unique=True 유일한 값으로 변경해주기
    #null=True빈값 입력가능하도록 하기
    department = models.CharField(max_length=30, null=True, default='')
    nickname = models.CharField(max_length=15, null=True, default='', error_messages={'unique': '이미 사용중인 닉네임입니다.'}) 
    #nickname = models.CharField(max_length=15, unique=True, null=True, default='', error_messages={'unique': '이미 사용중인 닉네임입니다.}) 
    
    phone_number = PhoneNumberField(null=True)
    

    #category를 폴린키로 가져올 수도 있을 것 같은디--> 계속 유저가 생성할 수 있게, 참조할 수 있게, 1대 다로 참조할 수 있게 구성
    category = models.ForeignKey(Category_Item, models.CASCADE, related_name="user_categorys", null=True, default='')
    email_period = models.ForeignKey(Email_period, models.CASCADE, related_name="user_emails", null=True, default='')
    # email_period = models.CharField(max_length=15, null=True, default="7") 
    is_active = models.BooleanField(default=True)
    is_premier = models.BooleanField(default=False)

    def __str__(self):
        return self.email
'''