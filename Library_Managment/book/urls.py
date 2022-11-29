from django.urls import path
from book import views

urlpatterns = [
    path('adddata/',views.adddata),
    path('softdelete/<int:tid>',views.softdelete),
    path('update/<int:tid>',views.update),
    path('ltoh/',views.ltoh),
    path('htol/',views.htol),
    path('all_data_include_soft_deleted/',views.all_data_include_soft_deleted),




]
