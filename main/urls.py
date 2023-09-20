from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import logout_user


app_name = 'main'

urlpatterns = [
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('create-product', create_product, name='create_product'),
    path('', show_main, name='show_main'),
]