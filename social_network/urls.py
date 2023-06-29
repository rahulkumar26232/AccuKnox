from django.urls import path
from rest_framework_simplejwt import views

from social_network.apis.friend_request import SendFriendRequestApi, AcceptFriendRequestApi, FriendsListApi, \
    PendingRequestsListApi
from social_network.apis.search_user import SearchUserApi
from social_network.apis.signup import UserSignupApi

urlpatterns = [
    path('signup/', UserSignupApi.as_view()),
    path('signin/', views.TokenObtainPairView.as_view()),
    path('user/search/', SearchUserApi.as_view({"get":"list"})),
    path('friend-request/send/', SendFriendRequestApi.as_view()),
    path('friend-request/accept/', AcceptFriendRequestApi.as_view(),name='accept-reject-friend-request'),
    path('friends/list/', FriendsListApi.as_view({"get":"list"})),
    path('friend-request/pending/list/', PendingRequestsListApi.as_view({"get":"list"})),
]
