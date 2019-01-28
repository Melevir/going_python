from django.urls import include, path
from django.contrib import admin
from poll.views import StartUserView, StartUserStatView

urlpatterns = [
    path('poll/', include('poll.urls')),
    path('admin/', admin.site.urls),
    path('user/started/', StartUserView.as_view()),
    path('user/started/stat/', StartUserStatView.as_view()),
]
