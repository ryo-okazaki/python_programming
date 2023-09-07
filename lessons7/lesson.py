from email import message
from email.mime import multipart
from email.mime import text
import smtplib

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'xxxxx@gmail.com'
to_email = 'xxxxxi@gmail.com'
username = 'xxxxx'
password = 'xxxxxx'

# msg = message.EmailMessage()
# msg.set_content('Test email')

msg = multipart.MIMEMultipart()

msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

msg.attach(text.MIMEText('Test email', 'plain'))

with open('lesson.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment', filename='lesson.py'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo() # SMTPサーバーに接続する
server.starttls() # 暗号化通信を行う
server.ehlo() # SMTPサーバーに接続する
server.login(username, password) # ログインする
server.send_message(msg) # メールを送信する
server.quit() # サーバーとの接続を閉じる