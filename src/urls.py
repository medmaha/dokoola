from django.contrib import admin

from django.urls import path, re_path, include
from django.http import HttpResponseRedirect, JsonResponse


def index(request):
    import os 
    CLIENT_SITE_ROUTE = os.environ.get("CLIENT_SITE_ROUTE")
    return HttpResponseRedirect(CLIENT_SITE_ROUTE)

def api_index(request):
    return JsonResponse({
        "message": "Welcome to Dokoola API",

    })

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/jobs/", include("jobs.urls")),
    path("api/users/", include("users.urls")),
    path("api/staffs/", include("staffs.urls")),
    path("api/clients/", include("clients.urls")),
    path("api/reviews/", include("reviews.urls")),
    path("api/proposals/", include("proposals.urls")),
    path("api/freelancers/", include("freelancers.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/messenging/", include("messenging.urls")),
    path("api/account/", include("users.account.urls")),
    re_path(r"^api*.", api_index),
    re_path(r".*", index),
]
