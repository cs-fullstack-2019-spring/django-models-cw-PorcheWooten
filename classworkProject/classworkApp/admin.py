from django.contrib import admin

# Register your models here.
from .models import Dog
from .models import Account
# register dog model(class)
admin.site.register(Dog)
# register account model
admin.site.register(Account)
