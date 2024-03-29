from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, Suber, IndexView
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', cache_page(60)(PostList.as_view()), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('sub/', Suber.as_view(), name='sub'),
   path('index/', IndexView.as_view()),
]
