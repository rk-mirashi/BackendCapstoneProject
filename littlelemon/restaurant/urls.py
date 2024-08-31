from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    #path('users', views.UserView.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/',views.BookingViewSet.as_view({'get' : 'list'})),
    path('api-token-auth/', obtain_auth_token),
]