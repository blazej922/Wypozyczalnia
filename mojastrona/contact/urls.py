from contact import views
from django.conf.urls import url, include

app_name='contact'
urlpatterns = [
    url(r'^$', views.send_message, name='send_message'),
]
