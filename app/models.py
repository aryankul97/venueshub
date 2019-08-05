from django.db import models
import datetime
class ImgData(models.Model):
	Hotel_ID=models.CharField(max_length=100)
	Image_Type=models.CharField(max_length=50)
	image=models.ImageField(upload_to="images/")
	class Meta:
		db_table="ImageData"
class HotelInfo(models.Model):
	Reg_Date=models.DateField(("Date"), default=datetime.date.today)
	Hotel_ID=models.CharField(max_length=100)
	Hotel_Name=models.CharField(max_length=200)
	Hotel_Address=models.TextField()
	Hotel_City=models.CharField(max_length=50)
	Hotel_Area=models.CharField(max_length=100)
	Hotel_State=models.CharField(max_length=100)
	Hotel_Phone=models.CharField(max_length=50)
	Hotel_Email=models.CharField(max_length=50)
	Hotel_PriceType=models.CharField(max_length=50)
	Hotel_Price=models.CharField(max_length=50)
	Hotel_Min_Gathering=models.CharField(max_length=50)
	Hotel_Max_Gathering=models.CharField(max_length=50)
	Hotel_Category=models.CharField(max_length=50)
	Hotel_Event_Type=models.CharField(max_length=50)
	Status=models.CharField(max_length=50)
	class Meta:
		db_table="HotelInfo"

class CategoryInfo(models.Model):
	Category_Name=models.CharField(max_length=100)
	class Meta:
		db_table="CategoryInfo"

class EventCategory(models.Model):
	Category_Name=models.CharField(max_length=100)
	class Meta:
		db_table="EventCategory"

class FacilityInfo(models.Model):
	Hotel_ID=models.CharField(max_length=100)
	Stage=models.CharField(max_length=10)
	DJ=models.CharField(max_length=10)
	Pool=models.CharField(max_length=10)
	Seating_Style=models.CharField(max_length=50)
	Caterer=models.CharField(max_length=10)
	Rental_Charge=models.CharField(max_length=10)
	Decoration_Included=models.CharField(max_length=10)
	Crokery_Included=models.CharField(max_length=10)
	Hall_Included=models.CharField(max_length=10)
	AC_Rooms=models.CharField(max_length=10)
	NON_AC_Rooms=models.CharField(max_length=10)
	Other_Terms=models.TextField()
	class Meta:
		db_table="FacilityInfo"

class DecorationTypeInfo(models.Model):
	Hotel_ID=models.CharField(max_length=100)
	Decoration_Name=models.CharField(max_length=100)
	Decoration_Price=models.CharField(max_length=100)
	class Meta:
		db_table="DecorationTypeInfo"