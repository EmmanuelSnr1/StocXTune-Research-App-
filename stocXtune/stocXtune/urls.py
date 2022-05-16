
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('watchlists.urls')),
    path('api/', include('watchlists_api.urls',namespace='watchlists_api')),
    path('api/user/', include('users.urls', namespace='users')),    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_obtain_pair'),
    path('techscanner/', include('techscanner.urls')),
    path('techscanner_api/', include('techscanner_api.urls')),
    #path('', include('watchlistsapi.urls', namespace='watchlistsapi')),
]
