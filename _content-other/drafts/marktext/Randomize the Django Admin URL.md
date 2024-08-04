# Randomize the Django Admin URL

---

tags: ["security", "django"]

---

The built-in admin panel URL defaults to `site.com/admin/`, making it a prime target for Web, scraping discovery, an automated brute force attacks.

Before putting your site live, this URL path should be changed to something that is not so easily discoverable.

## How to change the Django admin URL path

1. Go to your project's `urls.py` file

2. Add this block of code to randomize the admin path:

```python
# from django.urls import path, include
# from django.contrib import admin
# from django.conf import settings

# urlpatterns = [
#    ...
# ]


if settings.DEBUG:
    urlpatterns = [
    path("admin/", admin.site.urls),
] + urlpatterns


if not settings.DEBUG:
    urlpatterns = [
    path("77randomAdmin@33/", admin.site.urls),
] + urlpatterns
```

This code tells Django to change the admin URL from `admin/` to `77randomAdmin@33/` when DEBUG is set to FALSE, which will add one more layer of protection to your admin area.

>  Obviously you will want to replace `77randomAdmin@33/` in the code with something of your choosing - this is just an example.



---


