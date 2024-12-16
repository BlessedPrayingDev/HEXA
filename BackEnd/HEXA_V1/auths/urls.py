from django.urls import path
from auths.views import RegisterView, AllUserView, CheckLoginView, UserExist, UserInfo, UserInfoUpdate, UserDelete
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('users/', AllUserView.as_view()),
    path('register/' , RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 토큰 갱신
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('userexist/', UserExist.as_view()),
    path('userinfo/', UserInfo.as_view()),
    path('userinfoupdate/', UserInfoUpdate.as_view()),
    path('userdelete/', UserDelete.as_view()),
]