from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from .views import CreateUserView,Login

# define the router
router = DefaultRouter()

# define the router path and viewset to be used
router.register(r'signup', CreateUserView)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls')),
    path(r'get_token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
	path(r'refresh_token/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path(r'signin/', Login.as_view(), name="login"),
]