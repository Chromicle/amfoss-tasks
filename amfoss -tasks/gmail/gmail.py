import smtplib  #Set up the SMTP server for gmail 
import time
print("welcome to gmail")
time.sleep(1)
print("login to your gmail..")
time.sleep(2)
your=raw_input("enter your gmail: ")
print("proceding...")
time.sleep(2)
your1=raw_input("enter your password")
time.sleep(2)
sender=raw_input("eneter the sender")

msg =raw_input("enter the massage here") 



sub =raw_input("enter the subject here") 

server = smtplib.SMTP('smtp.gmail.com:587')

#host address and port number of your particular email 

server.starttls()

server.login(your,your1)

server.sendmail(your, sender, msg)

print("sending your mesage....")
time.sleep(2)

server.quit()

print("msg send sucessfully")




#ajayprabhakar369@gmail.com
