#1.将Python内置的模块(功能导入)
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

#2 .构建邮件内容
msg = MIMEText("领导早上好，领导今天辛苦了。","html","utf-8") #内容
msg["From"]=formataddr( [ "曾浩","zenghao518518@163.com" ]) #自己名字/自己邮箱
msg["to"]= "zenghao518518@163.com"  #目标邮箱
msg["Subject"] = "日常信息" #主题

#3.发送邮件
server =smtplib.SMTP_SSL("smtp.163.com" )
server.login ( "zenghao518518@163.com","OWWWVZANOTQKNIQA") #账户/授权码
#自己邮箱、目标邮箱
server.sendmail ( "zenghao518518@163.com","zenghao518518@163.com",msg.as_string())
server.quit()
