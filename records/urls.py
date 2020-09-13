from django.conf.urls.static import static
from django.urls import path

from ipams import settings
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='records-index'),
    path('record/<int:record_id>', views.ViewRecord.as_view(), name='records-view'),
    path('record/myrecords/<int:record_id>', views.MyRecordView.as_view(), name='records-myrecords-view'),
    path('record/pending/<int:record_id>', views.PendingRecordView.as_view(), name='records-pending-view'),
    path('record/approved/<int:record_id>', views.ApprovedRecordView.as_view(), name='records-approved-view'),
    path('record/declined/<int:record_id>', views.DeclinedRecordView.as_view(), name='records-declined-view'),
    path('add/', views.Add.as_view(), name='records-add'),
    path('uploadexcel/', views.ParseExcel.as_view(), name='records-upload'),
    path('downloadformat/', views.download_format, name='records-download-format'),
    path('download/abstract/<int:record_id>', views.download_abstract, name='records-download-abstract'),
    path('records/user/', views.MyRecordsView.as_view(), name='records-myrecords'),
    path('records/pending/', views.PendingRecordsView.as_view(), name='records-pending'),
    path('records/approved/', views.ApprovedRecordsView.as_view(), name='records-approved'),
    path('records/declined/', views.DeclinedRecordsView.as_view(), name='records-declined'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
