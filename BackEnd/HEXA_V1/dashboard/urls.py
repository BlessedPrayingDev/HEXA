from django.urls import path
from dashboard.views import GetHexaUsers, GetHexaOrders, GetHexaSessionUsers, RegisterHexaUser, HexaUserInfoUpdate, DeleteHexaUser, GetDockerContainers

urlpatterns = [
    path('hexausers/', GetHexaUsers.as_view()),
    path('hexaorders/', GetHexaOrders.as_view()),
    path('hexasessionuser/', GetHexaSessionUsers.as_view()),
    path('registerhexauser/', RegisterHexaUser.as_view()),
    path('hexauserinfoupdate/', HexaUserInfoUpdate.as_view()),
    path('deletehexauser/', DeleteHexaUser.as_view()),
    path('apidockercontainer/', GetDockerContainers.as_view()),
]