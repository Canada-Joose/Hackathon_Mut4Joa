# import smtplib
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# # from email.mime.application import MIMEApplication
# import django
from django.core.mail import EmailMessage
# from django.contrib.auth.models import User

content = """
    <html>
    <body>
        <h2>{title}</h2>
        <p>메일 전송 테스트입니다</p>
    </body>
    </html>
""".format(
title = '메일.. 받으셨나요..?'
)

email = EmailMessage(content,
    'toyoalsrl@likelion.org',     # 보내는 이메일 (settings에서 설정해서 작성안해도 됨)
    to=['kudocjoayo@gmail.com'],  # 받는 이메일 리스트
)
email.send()

# recipients = ["jiwoo091510@gmail.com"]

# message = MIMEMultipart();
# message['Subject'] = '메일 전송 테스트'
# message['From'] = "kudockudoc@gmail.com"
# message['To'] = ",".join(recipients)

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

# mimetext = MIMEText(content,'html')
# message.attach(mimetext)


# server = smtplib.SMTP('smtp.naver.com',587)
# server.ehlo()
# server.starttls()
# server.login(email_id,email_pw)
# server.sendmail(message['From'],recipients,message.as_string())
# server.quit()
