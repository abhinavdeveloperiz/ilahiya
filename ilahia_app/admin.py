from django.contrib import admin
from django.utils.html import format_html
from .models import Home, Academic_Program, Courses, Management_desk, Administrator_desk, Gallery,Faculty,Notice,Principal_desk


# Change the default Django admin titles
admin.site.site_header = "ILAHIALAWCOLLAGE"
admin.site.site_title = "ILAHIALAWCOLLAGE"
admin.site.index_title = "Welcome to ILAHIALAWCOLLAGE Admin Panel"



admin.site.register(Notice)


@admin.register(Principal_desk)
class PrincipalDeskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "message", "image_preview")
    search_fields = ("name", "message")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:6px;" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:6px;" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"


@admin.register(Academic_Program)
class AcademicProgramAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "image_preview")
    search_fields = ("description",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:6px;" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "description", "image_preview")
    search_fields = ("course", "description")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:6px;" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"


@admin.register(Management_desk)
class ManagementDeskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "position", "image_preview")
    search_fields = ("name", "position")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:6px;" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"


@admin.register(Administrator_desk)
class AdministratorDeskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "position", "image_preview")
    search_fields = ("name", "position")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:6px;" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="120" style="border-radius:6px;" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "designation", "image_preview")
    search_fields = ("name", "designation")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:6px;" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"



