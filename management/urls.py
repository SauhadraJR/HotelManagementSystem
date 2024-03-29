from django.urls import path
from .views import RoomTypeView
from .views import RoomView, RoomEditView, UserView, GroupView

urlpatterns = [
    path('room-type/',RoomTypeView.as_view({'get':'list','post':'create'})),
    path('room-type/<int:pk>/',RoomTypeView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('room/',RoomView.as_view()),
    path('room/<int:pk>/',RoomEditView.as_view()),
    path('register/',UserView.as_view({'post':'register'}),name = 'register'),
    path('login/',UserView.as_view({'post':'login'}),name = 'login'),
    path('role/',GroupView.as_view({'get':'list'}),name = 'role-listing')
]
