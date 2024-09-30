from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

usertypel = [
     ('1','user'),
    ('2','buyer'),
    ('3','seller'),
    ('4','rent'),

]
genderl = [
    ('male','male'),
    ('female','female'),

]
statusl = [

    ('0','Active'),
    ('1','Inactive'),
]
Quntityl = [

('1','1'),
('2','2'),
('3','3'),
('4','4'),
('5','5'),
('6','6'),
('7','7'),
('8','8'),
('9','9'),
('10','10'),
('11','11'),
('12','12'),
('13','13'),
('14','14'),
('15','15'),
('16','16'),
('1','17'),
('18','18'),
('19','19'),
('20','20'),

]
class role(models.Model):
    u_typename = models.CharField(max_length=30,choices=usertypel)



    def __str__(self):
        return self.u_typename
class user_detalis(models.Model):
    u_name = models.CharField(max_length=30)
    u_dp = models.ImageField(upload_to='photos')
    u_gender = models.CharField(max_length=30,choices=genderl)
    u_email = models.EmailField()
    u_phone = models.BigIntegerField()
    u_type = models.ForeignKey(role,on_delete=models.CASCADE)
    u_status = models.CharField(max_length=30,choices=statusl)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.u_dp.url))

    admin_photo.allow_tags = True

    def __str__(self):
        return self.u_name
class furniture(models.Model):
    cat_name = models.CharField(max_length=30)
    cat_picture = models.ImageField(upload_to='photos')
    cat_desc = models.TextField()
    category_added = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.cat_name
    def furniture_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.cat_picture.url))


    furniture_photo.allow_tags = True


class country(models.Model):
    co_name = models.CharField(max_length=30)

    def __str__(self):
        return  self.co_name
class state(models.Model):
    country_id = models.ForeignKey(country,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=30)

    def __str__(self):
        return self.state_name
class city(models.Model):
    state_id = models.ForeignKey(state,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name
class user_address(models.Model):
    u_id = models.ForeignKey(user_detalis,on_delete=models.CASCADE)
    building_name = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    city_name = models.ForeignKey(city,on_delete=models.CASCADE)
    pin_code = models.IntegerField()

class feedback_details(models.Model):
    f_title = models.CharField(max_length=30)
    f_desc = models.TextField()
    f_by = models.ForeignKey(user_detalis,on_delete=models.CASCADE)
    f_on = models.DateTimeField(auto_now=True,editable=False)


class complain(models.Model):
    c_name = models.CharField(max_length=30)
    c_detail = models.TextField()
    c_photo = models.ImageField(upload_to='photos')
    c_by = models.ForeignKey(user_detalis,on_delete=models.CASCADE)
    c_on = models.DateTimeField(auto_now=True,editable=False)

    def complain_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.c_photo.url))

    complain_photo.allow_tags = True
class brand_table(models.Model):
    brand_name = models.CharField(max_length=30)
    brand_desc = models.TextField()
    brand_logo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.brand_name

    def logo_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.brand_logo.url))

    logo_photo.allow_tags = True
class new_furniture(models.Model):
    furniture_model_name = models.CharField(max_length=30)
    brand_name = models.ForeignKey(brand_table,on_delete=models.CASCADE)
    furniture_desc = models.TextField()
    furniture_price = models.FloatField()
    furniture_image = models.ImageField(upload_to='photos')
    furniture_type = models.ForeignKey(furniture,on_delete=models.CASCADE)
    available_quntity = models.CharField(max_length=30,choices=Quntityl)

    def __str__(self):
        return self.furniture_model_name

    def furniture_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.furniture_image.url))

    furniture_photo.allow_tags = True


class old_furniture(models.Model):
    old_furniture_name = models.CharField(max_length=30)
    o_furniture_name = models.ForeignKey(brand_table,on_delete=models.CASCADE)
    old_furniture_desc = models.TextField()
    old_furniture_price = models.FloatField()
    old_furniture_image = models.ImageField(upload_to='photos')
    old_furniture_type = models.ForeignKey(furniture,on_delete=models.CASCADE)
    available_quntity = models.CharField(max_length=30,choices=Quntityl)

    def __str__(self):
        return self.old_furniture_name

    def old_furniture_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.old_furniture_image.url))

    old_furniture_photo.allow_tags = True


class rent_furniture(models.Model):
    rent_furniture_name = models.CharField(max_length=30)
    rentBrand_Name = models.ForeignKey(brand_table,on_delete=models.CASCADE)
    rent_furniture_desc = models.TextField()
    rent_furniture_price = models.FloatField()
    rent_furniture_image = models.ImageField(upload_to='photos')
    rent_furniture_type = models.ForeignKey(furniture,on_delete=models.CASCADE)
    available_quntity = models.CharField(max_length=30,choices=Quntityl)

    def __str__(self):
        return self.rent_furniture_name

    def rent_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.rent_furniture_image.url))

    rent_photo.allow_tags = True



class newfurniture_buying(models.Model):
    furniture_id = models.ForeignKey(new_furniture,on_delete=models.CASCADE)
    u_id = models.ForeignKey(user_detalis,on_delete=models.CASCADE)
    booking_datetime = models.DateTimeField(auto_now=True,editable=False)

class oldfurnoture_buying(models.Model):
    old_furniture_id = models.ForeignKey(old_furniture,on_delete=models.CASCADE)
    u_booking_id = models.ForeignKey(user_detalis,on_delete=models.CASCADE)
    old_booking_datetime = models.DateTimeField(auto_now=True,editable=False)

class rentfurniture_order(models.Model):
    rent_furniture = models.ForeignKey(rent_furniture,on_delete=models.CASCADE)
    rent_userid = models.ForeignKey(user_detalis,on_delete=models.CASCADE)
    rent_startdate = models.DateField()
    rent_enddate = models.DateField()
    rent_bookingdatetime = models.DateTimeField(auto_now=True,editable=False)

