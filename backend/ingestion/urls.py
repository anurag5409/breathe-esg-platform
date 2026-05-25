from django.urls import path
from .views import *


urlpatterns = [

    path(
        'upload/sap/',
        SAPUploadView.as_view()
    ),

    path(
        'reviews/',
        ReviewQueueView.as_view()
    ),

    path(
        'approve/<int:pk>/',
        ApproveRecordView.as_view()
    ),

    path(
        'upload/utility/',
        UtilityUploadView.as_view()
    ),

    path(
        'upload/travel/',
        TravelUploadView.as_view()
    ),
    ]