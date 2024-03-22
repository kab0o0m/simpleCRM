from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "leads"

urlpatterns = [
    path("", login_required(views.LeadListView.as_view()), name="lead-list"),
    path("<int:pk>/", views.LeadRetrieveUpdateDestroy.as_view(), name="lead-update"),
    path("view/", views.lead_list, name="view-list")

]
