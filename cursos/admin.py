from django.contrib import admin
from django.utils.html import format_html
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

class AulaInline(admin.StackedInline):
    model = Aula
    extra = 0

class ApostilaAdmin(admin.ModelAdmin):
    fields = ['titulo']
    inlines = [ApostilaNoSortableInline]
    search_fields = ['titulo']
    list_filter = ['created_at', 'updated_at']

class AulaAdmin(admin.ModelAdmin):
    inlines = [ApostilaInline]
    search_fields = ['titulo']
    raw_id_fields = ['curso']
    list_filter = ['created_at', 'updated_at']

class CursoAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="/{}" />'.format(obj.imagem.url))

    image_tag.short_description = 'Imagem'

    inlines = [AulaInline]
    search_fields = ['titulo']
    list_display = ['titulo', 'image_tag', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']

admin.site.register(Apostila, ApostilaAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Curso, CursoAdmin)
