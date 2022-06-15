from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from app import views as app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.index, name='index'),
    path('task/<int:id>/', app.show_task, name='task'),
    path('create-task/', app.create_task, name='create'),
    path('edit-task/<int:id>/', app.edit_task, name='edit'),
    path('saved-edited-task/', app.saved_edited_task, name='save_edited'),
    path('save-task/', app.save_task, name='save'),
    path('delete-task/<int:id>/', app.delete_task, name='delete')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
