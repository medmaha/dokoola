from django.contrib import admin

from django.urls import path, re_path, include
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse


def index(request, *args, **kwargs):
    import os 
    DEFAULT_ROUTE = "https://dokoola.vercel.app"
    CLIENT_SITE_ROUTE = os.environ.get("CLIENT_SITE_ROUTE", DEFAULT_ROUTE)
    return HttpResponseRedirect(CLIENT_SITE_ROUTE)
def not_found(request):
    return HttpResponse(
        "<h1>404 | Not Found!</h1>",
        status=404
    )

def api_index(request, *args, **kwargs):
    try:
        endpoint = args[0]
        if not endpoint:
            raise Exception("Endpoint not found")
        return JsonResponse({
            "Provider": "Dokoola",
            "message":"Oops! API endpoint not found",

        }, status=404)
    except:
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

    re_path(r"^api/?(.*)?/?$", api_index),
    path("", index),
    re_path(r".*", not_found),
]
