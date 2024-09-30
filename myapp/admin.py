from django.contrib import admin
from .models import role,user_detalis,furniture,country,state,city,user_address,feedback_details,complain,brand_table,new_furniture,old_furniture,rent_furniture,newfurniture_buying,oldfurnoture_buying,rentfurniture_order

# Register your models here.

class showrole(admin.ModelAdmin):
    list_display = ["u_typename"]

admin.site.register(role,showrole)

class showuser_details(admin.ModelAdmin):
    list_display = ["u_name","u_dp","u_gender","u_email","u_phone","u_type","u_status","admin_photo"]

admin.site.register(user_detalis,showuser_details)

class showfurniture(admin.ModelAdmin):
    list_display = ["cat_name","cat_picture","cat_desc","category_added","furniture_photo"]

admin.site.register(furniture,showfurniture)

class showcountry(admin.ModelAdmin):
    list_display = ["co_name"]

admin.site.register(country,showcountry)

class showstate(admin.ModelAdmin):
    list_display = ["country_id","state_name"]

admin.site.register(state,showstate)

class showcity(admin.ModelAdmin):
    list_display = ["state_id","city_name"]

admin.site.register(city,showcity)

class showuser_address(admin.ModelAdmin):
    list_display = ["u_id","building_name","street_name","city_name","pin_code"]

admin.site.register(user_address,showuser_address)

class showfeedback_details(admin.ModelAdmin):
    list_display = ["f_title","f_desc","f_by","f_on"]

admin.site.register(feedback_details,showfeedback_details)

class showcomplain_details(admin.ModelAdmin):
    list_display = ["c_name","c_detail","c_photo","c_by","c_on","complain_photo"]

admin.site.register(complain,showcomplain_details)

class showbrand_table(admin.ModelAdmin):
    list_display = ["brand_name","brand_desc","brand_logo","logo_photo"]

admin.site.register(brand_table,showbrand_table)

class shownew_furniture(admin.ModelAdmin):
    list_display = ["furniture_model_name","brand_name","furniture_desc","furniture_price","furniture_image","furniture_type","available_quntity","furniture_photo"]

admin.site.register(new_furniture,shownew_furniture)

class showold_furniture(admin.ModelAdmin):
    list_display = ["old_furniture_name","o_furniture_name","old_furniture_desc","old_furniture_price","old_furniture_image","old_furniture_type","available_quntity","old_furniture_photo"]

admin.site.register(old_furniture,showold_furniture)

class showrent_furniture(admin.ModelAdmin):
    list_display = ["rent_furniture_name","rentBrand_Name","rent_furniture_desc","rent_furniture_price","rent_furniture_image","rent_furniture_type","available_quntity","rent_photo"]

admin.site.register(rent_furniture,showrent_furniture)

class shownewfurniture_buying(admin.ModelAdmin):
    list_display = ["furniture_id","u_id","booking_datetime"]

admin.site.register(newfurniture_buying,shownewfurniture_buying)

class showoldfurnoture_buying(admin.ModelAdmin):
    list_display = ["old_furniture_id","u_booking_id","old_booking_datetime"]

admin.site.register(oldfurnoture_buying,showoldfurnoture_buying)

class showrentfurniture_order(admin.ModelAdmin):
    list_display = ["rent_furniture","rent_userid","rent_startdate","rent_enddate","rent_bookingdatetime"]

admin.site.register(rentfurniture_order,showrentfurniture_order)