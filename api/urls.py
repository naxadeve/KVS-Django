from django.urls import path, include
from django.conf.urls import url
from api.viewssets import core_viewsets, user_viewsets, front_viewsets
from rest_framework.routers import DefaultRouter
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='KVS API')

router = DefaultRouter()
router.register(r'house_hold', core_viewsets.HouseHoldViewSet)
router.register(r'family_members', core_viewsets.FamilyDetailViewSet)
router.register(r'animal_detail', core_viewsets.AnimalDetailViewSet)
# router.register(r'municipality', core_viewsets.MunicipalityViewSet)
router.register(r'users', user_viewsets.UserViewSet)
router.register(r'gallery', core_viewsets.GalleryViewSet)

#role
router.register(r'users_role', user_viewsets.RoleViewSet)


# front page api urls
router.register(r'header', front_viewsets.HeaderViewSet)
router.register(r'contact', front_viewsets.ContactViewSet)
router.register(r'mission', front_viewsets.OurMissionViewSet)
router.register(r'about', front_viewsets.AboutProjectViewSet)
router.register(r'system_features', front_viewsets.OverallSystemFeaturesViewSet)


# router.register(r'house_hold', core_viewsets.HouseHoldViewSet)
# router.register(r'animal_detail', core_viewsets.AnimalDetailViewSet)
# router.register(r'owner_family', core_viewsets.FamilyDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # url('swagger', schema_view),
    path('province_geo_json', core_viewsets.ProvinceGeojsonViewSet.as_view(), name='province-geojson'),
    path('district_geo_json', core_viewsets.DistrictGeojsonViewSet.as_view(), name='district-geojson'),
    path('municipality_geo_json', core_viewsets.MunicipalityGeojsonViewSet.as_view(), name='municipality-geojson'),

    # user related urls
    path('auth-token', user_viewsets.CustomAuthToken.as_view(), name='custom_token'),
    path('register', user_viewsets.Register.as_view(), name='register'),
    path('login', user_viewsets.UserLogIn.as_view(), name='login'),
    path('logout', user_viewsets.UserLogOut.as_view(), name='logout'),

    # core_urls
    path('overview', core_viewsets.OverviewViewSet.as_view(), name='overview'),
    path('unique', core_viewsets.UniqueValuesViewSet.as_view(), name='unique'),
    path('front', core_viewsets.FrontViewSet.as_view(), name='front'),
    # path('hdd', core_viewsets.HDDViewSet.as_view(), name='hdd'),
    path('more', core_viewsets.MoreViewSet.as_view(), name='more'),
    path('more_dropdown', core_viewsets.MoreDropDownViewSet.as_view(), name='drop'),
    path('fdd', core_viewsets.FddViewSet.as_view(), name='more'),
    path('highlight', core_viewsets.HighlightDataViewSet.as_view(), name='highlight'),

    #user list
    path('user_list', user_viewsets.UserListViewSet.as_view(), name='users_list'),
    path('user_dropdown', user_viewsets.CreateUserDropDownViewSet.as_view(), name='users_list'),

    #CSV file upload
    path('csv_upload', core_viewsets.CSVFileUploadHouseHold.as_view(), name='csv_upload'),

    #family_member_filter
    path('member_filter', core_viewsets.FamilyMemberFilterViewSet.as_view(), name='family_filter'),


    path('municipality', core_viewsets.MunicipalityViewSet.as_view(), name='municipality'),
    path('choices', core_viewsets.ChoiceViewSet.as_view(), name='choices'),



]
