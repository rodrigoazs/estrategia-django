from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Apostila, Curso, Aula

class ApostilaInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Aula.apostilas.through
    extra = 0
    raw_id_fields = ['apostila']

class ApostilaNoSortableInline(admin.TabularInline):
    model = Aula.apostilas.through
    extra = 0
    exclude = ['ordem']
    raw_id_fields = ['aula']

class ApostilaAdmin(admin.ModelAdmin):
    fields = ['titulo']
    inlines = [ApostilaNoSortableInline]


class AulaAdmin(admin.ModelAdmin):
    fields = ['titulo']
    inlines = [ApostilaInline]

admin.site.register(Apostila, ApostilaAdmin)
admin.site.register(Aula, AulaAdmin)
