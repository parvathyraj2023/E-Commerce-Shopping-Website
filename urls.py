from django.urls import path
from mainapp import views
urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('deletedata/<int:dataid>/',views.deletedata,name="deletedata"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:product_id>/',views.editproduct,name="editproduct"),
    path('updateproduct/<int:product_id>/',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name="deleteproduct"),
    path('adminloginpage/',views.adminloginpage,name="adminloginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('displaycontactdetails/',views.displaycontactdetails,name="displaycontactdetails"),
    path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact"),
    path('editcontact/<int:dataid>/',views.editcontact,name="editcontact"),
    path('updatecontact/<int:dataid>/', views.updatecontact, name="updatecontact")

]