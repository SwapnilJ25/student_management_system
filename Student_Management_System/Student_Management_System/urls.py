
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import Hod_Views, views , Staff_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE,name="base"),
    
    #Login path url
    path("",views.LOGIN ,name ="login" ),
    path("dologin/",views.doLOGIN ,name ="dologin" ),
    path("dologout/",views.doLogout ,name ="logout" ),
    
    #Profile Update
    path("profile",views.PROFILE ,name ="profile" ),
    path("profile/update",views.PROFILE_UPDATE ,name ="profile_update" ),
    
    
    #This is HOD panel  url
    path("Hod/Home",Hod_Views.HOME ,name ="hod_home" ),
    path("Hod/Student/Add",Hod_Views.ADD_STUDENT ,name ="add_student" ),
    path("Hod/Student/View",Hod_Views.VIEW_STUDENT ,name ="view_student" ),
    path("Hod/Student/Edit/<str:id>",Hod_Views.EDIT_STUDENT ,name ="edit_student" ),
    path("Hod/Student/Update",Hod_Views.UPDATE_STUDENT ,name ="update_student" ),
    path("Hod/Student/Delete/<str:admin>",Hod_Views.DELETE_STUDENT ,name ="delete_student" ),
    
    path("Hod/Course/Add",Hod_Views.ADD_COURSE ,name ="add_course" ),
    path("Hod/Course/View",Hod_Views.VIEW_COURSE ,name ="view_course" ),
    path("Hod/Course/Edit/<str:id>",Hod_Views.EDIT_COURSE ,name ="edit_course" ),
    path("Hod/Course/Update",Hod_Views.UPDATE_COURSE ,name ="update_course" ),
    path("Hod/Course/Delete/<str:id>",Hod_Views.DELETE_COURSE ,name ="delete_course" ),
    
    path("Hod/Staff/Add",Hod_Views.ADD_STAFF ,name ="add_staff" ),
    path("Hod/Staff/View",Hod_Views.VIEW_STAFF ,name ="view_staff" ),
    path("Hod/Staff/Edit/<str:id>",Hod_Views.EDIT_STAFF ,name ="edit_staff" ),
    path("Hod/Staff/Update",Hod_Views.UPDATE_STAFF ,name ="update_staff" ),
    path("Hod/Staff/Delete/<str:admin>",Hod_Views.DELETE_STAFF ,name ="delete_staff" ),
    
    
    path("Hod/Subject/Add",Hod_Views.ADD_SUBJECT ,name ="add_subject" ),
    path("Hod/Subject/View",Hod_Views.VIEW_SUBJECT ,name ="view_subject" ),
    path("Hod/Subject/Edit/<str:id>",Hod_Views.EDIT_SUBJECT ,name ="edit_subject" ),
    path("Hod/Subject/Update",Hod_Views.UPDATE_SUBJECT ,name ="update_subject" ),
    path("Hod/Subject/Delete/<str:id>",Hod_Views.DELETE_SUBJECT ,name ="delete_subject" ),
    
    
    path("Hod/Session/Add",Hod_Views.ADD_SESSION ,name ="add_session" ),
    path("Hod/Session/View",Hod_Views.VIEW_SESSION ,name ="view_session" ),
    path("Hod/Session/Edit/<str:id>",Hod_Views.EDIT_SESSION ,name ="edit_session" ),
    path("Hod/Session/Update",Hod_Views.UPDATE_SESSION ,name ="update_session" ),
    path("Hod/Session/Delete/<str:id>",Hod_Views.DELETE_SESSION ,name ="delete_session" ),
    
    path("Hod/Staff/Send_Notification",Hod_Views.STAFF_SEND_NOTIFICATION ,name ="staff_send_notification" ),
    path("Hod/Staff/Save_Notification",Hod_Views.SAVE_STAFF_NOTIFICATION ,name ="save_staff_notification" ),
    
    
    #This is STAFF panel  url
    path("Staff/Home",Staff_Views.HOME ,name ="staff_home" ),
    
    
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
