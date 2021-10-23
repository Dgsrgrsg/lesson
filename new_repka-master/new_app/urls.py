from django.urls import path

from new_app.views import stock_list


urlpatterns = [
    path('list/', stock_list)
]
