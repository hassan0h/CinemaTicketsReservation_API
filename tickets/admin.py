from django.contrib import admin
from .models import Guest, Movie, Reservation, Post

admin.site.register(Movie)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Post)
