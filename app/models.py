from django.db import models

# Create your models here.
class Country(models.Model):
    country_code=models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=10,unique=True)
    country_pop=models.IntegerField()
    country_area=models.IntegerField()
    country_info=models.URLField()
    

class Capital(models.Model):
    con_id=models.OneToOneField(Country,on_delete=models.CASCADE)
    capital_name=models.CharField(max_length=10,unique=True)
    no_of_cities=models.IntegerField()
    cap_city_pop=models.IntegerField()
    cap_announc_date=models.DateField()
    


    
