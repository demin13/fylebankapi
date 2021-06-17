from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/bank',views.showbank,name='showbank'),
    #path('api/bank/autocomplete',views.bankList.as_view()),
    path('api/branches/autocomplete',views.branchList.as_view()),
    path('api/branches',views.branchList1.as_view()),
]
