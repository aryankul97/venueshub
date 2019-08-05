from app.models import *

def gethoteldata():
	obj=HotelInfo.objects.all()
	lt=[]
	dic={}
	for elt in obj:
		dic={
			'Registration_Date':elt.Reg_Date,
			'Hotel_ID':elt.Hotel_ID,
			'Hotel_Name':elt.Hotel_Name,
			'Hotel_City':elt.Hotel_City,
			'Hotel_Area':elt.Hotel_Area,
			'Hotel_Email':elt.Hotel_Email,
			'Hotel_Phone':elt.Hotel_Phone
		}
		lt.append(dic)
	return lt

def getvenuecategories():
	obj=CategoryInfo.objects.all()
	lt=[]
	dic={}
	x=1
	for elt in obj:
		dic={
			'Sr':str(x),
			'Name':elt.Category_Name,
		}
		lt.append(dic)
		x=x+1
	return lt

def geteventcategories():
	obj=EventCategory.objects.all()
	lt=[]
	dic={}
	x=1
	for elt in obj:
		dic={
			'Sr':str(x),
			'Name':elt.Category_Name,
		}
		lt.append(dic)
		x=x+1
	return lt
def GetVenueID(name):
	obj=HotelInfo.objects.filter(Hotel_Name=name)
	hid=""
	for x in obj:
		hid=x.Hotel_ID
	return hid
def GetPriceType(name):
	obj=HotelInfo.objects.filter(Hotel_ID=name)
	ptype=""
	for x in obj:
		a=x.Hotel_PriceType
		if a=="Per Plate/Person":
			ptype='per plate'
		elif a=="Package Pricing":
			ptype='per night'
	return ptype