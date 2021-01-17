from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from users.urls import router as users_router

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('token/auth/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('docs/', include_docs_urls(title='Towing API')),
    path('password/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('', include(users_router.urls))
]
