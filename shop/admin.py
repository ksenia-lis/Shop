from django.contrib import admin

from .models import ManufacturerCountry
admin.site.register(ManufacturerCountry)

from .models import producer
admin.site.register(producer)

from .models import product
admin.site.register(product)

from .models import category
admin.site.register(category)

from .models import order
admin.site.register(order)

from .models import comment
admin.site.register(comment)