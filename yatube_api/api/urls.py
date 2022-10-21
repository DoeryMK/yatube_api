from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(r'posts\/(?P<post_id>\d+)\/comments',
                   CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path(
        'v1/follow/',
        FollowViewSet.as_view({'get': 'list', 'post': 'create', })
    ),
    path('v1/', include('djoser.urls.jwt')),
]
