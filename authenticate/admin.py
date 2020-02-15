from django.contrib import admin
from authenticate.models import UserProfileInfo,OperatorWindow,User,operator_skill_matrix
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(OperatorWindow)
admin.site.register(operator_skill_matrix)
