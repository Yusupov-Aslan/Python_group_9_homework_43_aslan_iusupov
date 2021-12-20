from django.urls import path

from webapp.views import index_view, result_view

urlpatterns = {
    path('', index_view),
    path('', result_view)
}
