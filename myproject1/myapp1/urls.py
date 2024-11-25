from django.contrib import admin
from django.urls import path,include
from myapp1 import views
#from rest_framework.routers import DefaultRouter
#from .views import ItemViewSet
#router = DefaultRouter()
#router.register(r'items', ItemViewSet)
'''
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)
'''


urlpatterns = [
    path('', views.add_db, name='add_db'),
    #path('success/', views.success, name='success'),
    #path("update/<str:pername>/<str:perage>/",views.update,name="update"),
    #path('delete/<str:pername>/<str:perage>/',views.delete,name='delete'),
    #path('',views.post_list, name='post_list'),
    #path('post/<int:pk>/',views.post_detail, name='post_detail'),
    #path('', views.index, name='index'),
    #path('set_name/', views.set_name, name='set_name'),
    #path('delete_name/', views.delete_name, name='delete_name'),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('example/', views.example_view, name='example'),
    #path('',include(router.urls)),
    #path('',views.user_info, name='user_info'),

]