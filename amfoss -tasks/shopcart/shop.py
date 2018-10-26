from PIL import Image   #after insatalling pillow we can import image for opening any image
import random  #i imported random function from library
import time	#imported time function for using the sleep function


print("welcome to shopping mall")

time.sleep(2)

print("choices are:1.hand kercheif ..../50  2.milk ...//24 3.vegetables .../100 4.grocery ...../100 7.finished ..../400 5.cell phone .../ 4000 6.dresses..../")

cost=0
flag=1
while(flag==1): #for infinitely running loop i given flag==1 untill you give fininshed as input
	inp=input()
	if(inp=="1"):
		if(input("are you conformed to add to cart 1.ok 2.no")=="1"):
			cost=cost+50
			print("hand kercheif is added to card")
		else:
			cost=cost
			print("it is removed from your cart")          #it will removes from your cart when you press other than 1


#for each item i given for conformation for to add to cart for all inputs i used this same type
	elif(inp=="2"):
		if(input("are you conformed to add to cart 1.ok 2.no")=="1"):
			cost=cost+24
			print(" it is added to card")
			time.sleep(1)
		else:
			cost=cost
			print("it is removed from your cart")
	elif(inp=="3"):
		
		time.sleep(1)
		if(input("are you conformed to add to cart 1.ok 2.no")=="1"):
			cost=cost+100
			print(" it is added to card")
			time.sleep(1)
		else:
			cost=cost
			print("it is removed from your cart")
		
	elif(inp=="4"):
		
		time.sleep(1)
		if(input("are you conformed to add to cart 1.ok 2.no")=="1"):
			cost=cost+100
			print(" it is added to card")
			time.sleep(1)
		else:
			cost=cost
			print("it is removed from your cart")
	elif(inp=="5"):
	
		time.sleep(1)
		if(input("are you conformed to add to cart 1.ok 2.no")=="1"):
			cost=cost+4000
			print(" it is added to card")
			time.sleep(1)
		else:
			cost=cost
			print("it is removed from your cart")
	elif(inp=="7"):
		break  #to exit out of loop

	elif(inp=="6"):             #given here is a small special we can enter the soo many loops
		time.sleep(2)   
		print("1.mens wear.... 2.women wear... 3.kids wear../") #asking which type they want
		he=(input("which type you want"))
		time.sleep(2)
		if(he=="1"):
			print("1.kurthas 2.jeans 3.pants") #which type of wear they want
			want=input("enter the type here")
			if(want=="1"):
				size=int(input())
				print("cost is 450")
				time.sleep(1)
				cost=cost+450
			elif(want=="2"):
				size=int(input())
				print("cost is 450")
				time.sleep(1)
				cost=cost+450
			
			else:
				size=int(input())
				print("cost is 990")
				time.sleep(1)
				cost=cost+990
				
		elif(he=="2"):
			print("1.shirts 2.chudidar 3.pants")
			want=input("enter the type here")
			if(want=="1"):
				size=int(input())
				print("cost is 450")
				time.sleep(1)
				cost=cost+450
				
			elif(want=="2"):
				size=int(input())
				print("cost is 450")
				time.sleep(1)
				cost=cost+450
				
			else:
				size=int(input())
				print("cost is 990")
				time.sleep(1)
				cost=cost+990

		elif(he=="3"):
			print("1.shirts 2.shorts 3.pants")
			time.sleep(2)
			want=input("enter the type here")
			if(want=="1"):
				size=int(input())
				print("cost is 450")
				cost=cost+450
			
			elif(want=="2"):
				size=int(input())
				print("cost is 450")
				time.sleep(1)
				cost=cost+450
				
			else:
				size=int(input())
				print("cost is 990")
				time.sleep(1)
				cost=cost+990
		else:
			print("item not avalible.. sorry")
				
	else:
		print("item is not avalible")
time.sleep(1)
print("is any coupan is available:")
coupan=input()
if(coupan=="fest"):			#giving the discount based on coupan card
	cost=cost-cost*4/100
	cost=round(cost)
else:
	cost=cost
print(cost)

img=Image.open("./image.jpg")  #to open image of jpg 
img.show()			#to show the image
img.close()			# to close image

while(flag==1):
	captcha=input("enter here:  ")
	if(captcha=="captcha"):
		print("correct captcha")
		break
	else:
		print("wrong captcha")
		
	
	
print("lets proceed to payment........")


time.sleep(2)
print("how do you pay bill")
time.sleep(1)
print("1.card 2.cash") #asking for which type to pay
time.sleep(1)
n=int(input())
if(n==1):
	

	print("1.visacard 2.mastercard 3.mastereo 4.rupaycard")        #asking the card type when selected as card
	card=int(input("select your card"))
	if(card==1 or 2 or 3 or 4):
		while(flag==1):
			ask=(input("enter your 12 digit card number")) #given the card number as 12 digits so upto when we entered the 12 then only it stop woring 
			if(len(ask)==12):
				break
			else:
				flag=1

		time.sleep(1)
		print("thank you")
		while(flag==1):
			mee=input("enter your card expiriy card")                #this is also like card number and given cvv numbers as 5 numbers
			if(len(mee)==5):
				break
			else:
				flag=1
		time.sleep(1)
		while(flag==1):
			cvv=input("enter your cvv")
			if(len(cvv)==3):
				break
			else:
				flag=1
		time.sleep(1)
		print("proceding your payment.......")
		time.sleep(3)
		print("payment done")
		print("thank you")
elif(n==2):
	print(cost)
	print("thank you")
		
