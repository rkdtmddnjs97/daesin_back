from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from user.views import ConfirmEmailView

schema_view = get_schema_view(
    openapi.Info(
        title='Daesin API',
        default_version='v1',
        description='daesin api',
        contact=openapi.Contact(email='leahpar0401@kookmin.ac.kr'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/verify-email/', ConfirmEmailView.as_view(), name="rest_resend_email"),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # swagger 설정
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path("admin/", admin.site.urls),
    path('post/', include('post.urls'), name='posts'),
    path('user/', include('user.urls'), name='users'),
    path('review/', include('review.urls'), name="reviews"),
    path('advertisement/', include('ad.urls'), name='ads'),
    path('club/', include('club.urls'), name="clubs"),
    path('comment/', include('relationship.urls.comment'), name="comments"),
    path('like/', include('relationship.urls.like'), name="likes"),
    path('scrap/', include('relationship.urls.scrap'), name="scraps"),
    path('tag/',include('tag.urls')),
    path('notice/', include('notice.urls'), name="notices"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
