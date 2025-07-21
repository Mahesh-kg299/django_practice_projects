from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import SignUpView, CompanyViewSet, IndustryViewSet

router = routers.DefaultRouter()
router.register("companies", CompanyViewSet)
router.register("industries", IndustryViewSet)

urlpatterns = [
    path("api-token/", views.obtain_auth_token),
    path("signup/", SignUpView.as_view()),
    path("", include(router.urls)),
    path("login/", include("rest_framework.urls"))
    # path("companies/", views.CompanyList.as_view()),
    # path("companies/<pk>/", views.CompanyDetail.as_view()),
    # path("industries/", views.IndustryList.as_view()),
    # path("industries/<pk>/", IndustryDetail.as_view())
]