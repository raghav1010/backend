from django.urls import path
# from . import views


# urlpatterns =[
#      path('',views.BusinessListAPIView.as_view(),name ="Business"),
#      path('<int:id>',views.BusinessDetailAPIView.as_view(),name ="Business"),
# ]

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'business', BusinessViewSet, basename="business")
router.register(r'employee',EmployeeView,basename="employee")

urlpatterns = router.urls 
