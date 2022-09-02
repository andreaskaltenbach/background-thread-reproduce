from django.contrib import admin
from dummy.models import Dummy

import threading
import time


def run():
    print("Run")
    millis = 0
    while millis <= 60000:
        print(f"{millis} milliseconds passed")
        dummy = Dummy.objects.all()
        print(len(dummy))
        time.sleep(0.2)
        millis += 200
        dummy = Dummy.objects.all()
        print(len(dummy))
    print("One minute passed. Done")


# Register your models here.
class DummyAdmin(admin.ModelAdmin):
    list_display = ('name',)

    actions = ('run_task',)

    def run_task(self, request, queryset):
        t = threading.Thread(target=run,
                             args=[])
        t.setDaemon(True)
        t.start()


admin.site.register(Dummy, DummyAdmin)
