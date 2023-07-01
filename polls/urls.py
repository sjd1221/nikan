from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name= "nikan"


urlpatterns = [
    path("", views.loginpage, name="login"),
    path("tableshow/<int:id>", views.tableshow, name="tableshow"),
    path('loginUser', views.loginUser, name='loginUser'),
    path("adddoctor", views.adddoctor, name='adddoctor'),
    path("removeduplicate", views.removeduplicate, name='removeduplicate')

]



urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
