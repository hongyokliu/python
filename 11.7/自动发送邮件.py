import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'ls614975618@163.com'
msg['to'] = '614975618@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。
'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('ls614975618@163.com', '051255775726qq')
smtp.sendmail('ls614975618@163.com', '614975618@qq.com', str(msg))
