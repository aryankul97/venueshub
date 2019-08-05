from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from app.models import *
from app.form import *
from app.hotelutil import *

def home(request):
	#obj=HotelInfo.objects.all().delete()
	return render(request,'index.html',{})
def about(request):
	return render(request,'about.html',{})
def adminLogin(request):
	return render(request,'adminLogin.html',{})
@csrf_exempt
def admincheck(request):
	if request.method=="POST":
		obj=HotelInfo.objects.all()
		i=request.POST.get("adminID")
		p=request.POST.get("adminpass")
		if i=="admin@venueshub.in" and p=="venueshub@admin":
			request.session['adminID'] = "admin@venueshub.in"
			request.session['adminpass'] = "venueshub@admin"
			dic={'hoteldata':gethoteldata(),
				'venuecategory':getvenuecategories(),
				'eventcategory':geteventcategories()}
			return render(request,'admindash.html', dic)
		else:
			return render(request,'adminLogin.html',{})
	return render(request,'adminLogin.html',{})
@csrf_exempt
def hoteldatasave(request):
	if request.method=="POST":
		name=request.POST.get("name")
		address=request.POST.get("address")
		city=request.POST.get("city")
		area=request.POST.get("area")
		address=request.POST.get("address")
		contact=request.POST.get("contact")
		email=request.POST.get("email")
		pricetype=request.POST.get("pricetype")
		price=request.POST.get("price")
		min=request.POST.get("min")
		max=request.POST.get("max")
		state=request.POST.get("state")
		status="N"
		obj=CategoryInfo.objects.all()
		category=""
		for x in obj:
			a=request.POST.get(x.Category_Name)
			if a!=None:
				category=category+a+' '
		obj=EventCategory.objects.all()
		ecategory=""
		for x in obj:
			a=request.POST.get(x.Category_Name)
			if a!=None:
				ecategory=ecategory+a+' '
		
		h="H00"
		x=1
		hid=h+str(x)
		while HotelInfo.objects.filter(Hotel_ID=hid).exists():
			x=x+1
			hid=h+str(x)
		x=int(x)

		obj=HotelInfo(
			Hotel_ID=hid,
			Hotel_Name=name,
			Hotel_Address=address,
			Hotel_City=city,
			Hotel_Area=area,
			Hotel_State=state,
			Hotel_Phone=contact,
			Hotel_Email=email,
			Hotel_PriceType=pricetype,
			Hotel_Price=price,
			Hotel_Min_Gathering=min,
			Hotel_Max_Gathering=max,
			Hotel_Category=category,
			Hotel_Event_Type=ecategory,
			Status=status
			)
		obj.save()
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved'+b2
		return render(request,'admindash.html',{'alert':alert})
@csrf_exempt
def addcategory(request):
	if request.method=="POST":
		c=request.POST.get('cname')
		obj=CategoryInfo(Category_Name=c)
		obj.save()
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved'+b2
		return render(request,'admindash.html',{'alert':alert})
@csrf_exempt
def addeventcategory(request):
	if request.method=="POST":
		c=request.POST.get('ename')
		obj=EventCategory(Category_Name=c)
		obj.save()
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved'+b2
		return render(request,'admindash.html',{'alert':alert})
#to open the page of adding venue
def addhotel(request):
	adminID = request.session['adminID']
	adminpass = request.session['adminpass']
	if adminID=="admin@venueshub.in" and adminpass=="venueshub@admin":
		dic={}
		lt=[]
		lt2=[]
		obj=CategoryInfo.objects.all()
		for elt in obj:
			lt.append(elt.Category_Name)
		obj=EventCategory.objects.all()
		for elt in obj:
			lt2.append(elt.Category_Name)
		dic={'category':lt,'ecategory':lt2}
		return render(request,'addhotel.html',dic)
#to open the page of adding decoration type to venue
def adddecoration(request):
	adminID = request.session['adminID']
	adminpass = request.session['adminpass']
	if adminID=="admin@venueshub.in" and adminpass=="venueshub@admin":
		dic={}
		lt=[]
		lt1=[]
		obj=FacilityInfo.objects.filter(Decoration_Included='Yes')
		for elt in obj:
			lt.append(elt.Hotel_ID)
		for elt in lt:
			obj=HotelInfo.objects.filter(Hotel_ID=elt)
			for x in obj:
				lt1.append(x.Hotel_Name)
		dic={'venuename':lt1}
	return render(request,'adddecoration.html',dic)
@csrf_exempt
def savedecoration(request):
	if request.method=="POST":
		vname=request.POST.get("venuename")
		obj=HotelInfo.objects.filter(Hotel_Name=vname)
		vid=""
		for x in obj:
			vid=x.Hotel_ID
		dname=request.POST.get("decorationname")
		dprice=request.POST.get("decorationprice")
		obj=DecorationTypeInfo(
			Hotel_ID=vid,
			Decoration_Name=dname,
			Decoration_Price=dprice,
			)
		obj.save()
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved'+b2
		return render(request,'admindash.html',{'alert':alert})
#to open the page of adding facility venue
def addfacility(request):
	adminID = request.session['adminID']
	adminpass = request.session['adminpass']
	if adminID=="admin@venueshub.in" and adminpass=="venueshub@admin":
		dic={}
		lt=[]
		obj=HotelInfo.objects.all()
		for elt in obj:
			lt.append(elt.Hotel_Name)
		dic={'venuename':lt}
		return render(request,'addfacility.html',dic)
@csrf_exempt
def facilitiesdatasave(request):
	if request.method=="POST":
		vname=request.POST.get("venuename")
		obj=HotelInfo.objects.filter(Hotel_Name=vname)
		vid=""
		for x in obj:
			vid=x.Hotel_ID
		stage=request.POST.get("stage")
		dj=request.POST.get("DJ")
		seatstyle=request.POST.get("seatstyle")
		caterer=request.POST.get("caterer")
		crokery=request.POST.get("crokery")
		pool=request.POST.get("pool")
		decoration=request.POST.get("decoration")
		hall=request.POST.get("hall")
		acrooms=request.POST.get("acrooms")
		nonacrooms=request.POST.get("nonacrooms")
		rental=request.POST.get("rental")
		TandC=request.POST.get("TandC")
		obj=FacilityInfo(
			Hotel_ID=vid,
			Stage=stage,
			DJ=dj,
			Pool=pool,
			Seating_Style=seatstyle,
			Caterer=caterer,
			Crokery_Included=crokery,
			Rental_Charge=rental,
			Decoration_Included=decoration,
			Hall_Included=hall,
			AC_Rooms=acrooms,
			NON_AC_Rooms=nonacrooms,
			Other_Terms=TandC
			)
		obj.save()
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved'+b2
		return render(request,'admindash.html',{'alert':alert})
#To Upload Image
def addimageopen(request):
	adminID = request.session['adminID']
	adminpass = request.session['adminpass']
	if adminID=="admin@venueshub.in" and adminpass=="venueshub@admin":
		dic={}
		lt=[]
		obj=HotelInfo.objects.all()
		for elt in obj:
			lt.append(elt.Hotel_Name)
		dic={'venuename':lt}
		return render(request,'addimage.html',dic)
@csrf_exempt
def saveimage(request):
	if request.method=="POST":
		form=ImageUploadForm(request.POST, request.FILES)
		vid=GetVenueID(request.POST.get("venuename"))
		if form.is_valid():
			m=form.cleaned_data['image']
			obj=ImgData(Hotel_ID=vid,image=m,Image_Type=request.POST.get('itype'))
			obj.save()
			dic={}
			lt=[]
			obj=HotelInfo.objects.all()
			for elt in obj:
				lt.append(elt.Hotel_Name)
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Saved'+b2
			dic={'venuename':lt,'alert':alert}
			return render(request,'addimage.html',dic)
def show(request):
	obj=ImgData.objects.all()
	path=''
	for elt in obj:
		path=elt.image.url
	print(path)
	return render(request,'image.html',{'path':path})
#to open venue catelog
def browsevenues(request):
	obj=HotelInfo.objects.all()
	lt=[]
	dic={}
	for x in obj:
		obj=ImgData.objects.filter(Hotel_ID=x.Hotel_ID)
		path=''
		for elt in obj:
			path=elt.image.url
		dic={'Hotel_Name':x.Hotel_Name,
			'Hotel_Price':x.Hotel_Price,
			'Hotel_PriceType':GetPriceType(x.Hotel_ID),
			'Hotel_City':x.Hotel_City,
			'Hotel_Area':x.Hotel_Area,
			'Hotel_Max_Gathering':x.Hotel_Max_Gathering,
			'Hotel_ID':x.Hotel_ID,
			'Image_Path':path}
		lt.append(dic)
	return render(request,'browsevenues.html',{'hdata':lt})
@csrf_exempt
def moreInfo(request):
	if request.method=="POST":
		vID=request.POST.get('vID')
		return HttpResponse(vID)