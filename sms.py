import requests

n = input("Enter Your Number: ")
a = int(input ("Enter Your Amount: "))


for i in range (a):
	r= requests.get("http://deepitsolution.in/api.php?number="+n)
	f= r.content
	print(f)
  