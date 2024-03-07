from django.urls import path
from.import views

urlpatterns = [

    path("ttmhome", views.ttmhome, name="ttmhome"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("checkRegistration",views.checkregistration,name="checkregistration"),
    path("viewplaces",views.viewplaces,name="viewplaces"),
    path("checkchangepassword",views.checkchangepassword,name="checkchangepassword"),

]
