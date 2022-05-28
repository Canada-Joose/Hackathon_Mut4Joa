from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime
from django.utils.dateformat import DateFormat
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
    # content = """
    #     <html>
    #     <body>
    #         <h2>{title}</h2>
    #         <p>메일 전송 테스트입니다</p>
    #     </body>
    #     </html>
    # """.format(
    # title = '메일.. 받으셨나요..?'
    # )
    # message = render_to_string('appMain/emailform.html')
    # mail_title = "과연 될까요?"
    # mail_to = "jiwoo091510@korea.ac.kr"
    # email = EmailMessage(mail_title, message, to= [mail_to])
    

    
    notices = Notice.objects.all()
    
    email = EmailMessage(

    'kudocjoayo@gmail.com',     
    render_to_string('appMain/emailform.html', {
        'notices':notices
        }),
    # 보내는 이메일 (settings에서 설정해서 작성안해도 됨)
    to=['jiwoo091510@gmail.com'],  # 받는 이메일 리스트

    )
    email.content_subtype= 'html'
    email.send()

    return render(request, "appMain/index.html")


def profile(request):
    return render(request, "appMain/profile.html")


def profileEdit(request):
    return render(request, "appMain/profileEdit.html")


def notice(request):
    return render(request, "appMain/notice.html")

def noticeDetail(request):
    return render(request, "appMain/noticeDetail.html")

now = datetime.now()
print (datetime.now().strftime('%y-%m-%d'))