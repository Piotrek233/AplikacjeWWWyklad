from django.urls import path
from .views import RatingList
from .views import EquipmentList
from .views import RatingDetail
from .views import EquipmentDetail
from .views import ApiRoot
from .views import UserList
from .views import UserDetail

urlpatterns = [
    path('equipment',EquipmentList.as_view(), name=EquipmentList.name),
    path('rating', RatingList.as_view(), name= RatingList.name),
    path('rating/<int:pk>',RatingDetail.as_view(), name=RatingDetail.name),
    path('equipment/<int:pk>', EquipmentDetail.as_view(), name=EquipmentDetail.name),
    path('users', UserList.as_view(), name=UserList.name),
    path('users/<int:pk>', UserDetail.as_view(), name=UserDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    ]
