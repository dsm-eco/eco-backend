from django.urls import path

from mypage.views import MyShopPostListViewSet, MyEventPostListViewSet

shop_post_list = MyShopPostListViewSet.as_view({'get': 'list'})
event_post_list = MyEventPostListViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('shop/', shop_post_list, name='shop-post-list'),
    path('event/', event_post_list, name='event-post-list'),
]

