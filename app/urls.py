from django.urls import path
from .views import WantDetail, WantUpdate, WantCreate, WantDelete, signupfunc, loginfunc, logoutfunc, listfunc, randomfunc, resultfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>', WantDetail.as_view(), name='detail'),
    path('result/', resultfunc, name='result'),
    path('update/<int:pk>', WantUpdate.as_view(), name='update'),
    path('create/', WantCreate.as_view(), name='create'),
    path('delete/<int:pk>', WantDelete.as_view(), name='delete'),
    path('random/', randomfunc, name='random'),
]
