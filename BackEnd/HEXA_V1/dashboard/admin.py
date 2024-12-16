from django.contrib import admin
from .models import hexaOrder, hexaUser, hexaSessionUsers, hexaModelWeight, hexaServer

# Register your models here.
admin.site.register(hexaOrder)
admin.site.register(hexaUser)
admin.site.register(hexaSessionUsers)
admin.site.register(hexaModelWeight)
admin.site.register(hexaServer)
