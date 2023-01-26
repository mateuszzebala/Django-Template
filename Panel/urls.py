from django.urls import path, re_path

from Panel.views import panel
from Panel.views.database import Database
from Panel.views.editor import Editor
from Panel.views.server import Server
from Panel.views.python import Python
from Panel.views.terminal import Terminal
from Panel.views.users import Users
from Panel.views.forms import Forms
from Panel.views.messages import Messages
from Panel.views.pages import Pages
from Panel.views.charts import Charts
from Panel.views.media import Media
from Panel.views.languages import Languages

app_name = 'Panel'


urlpatterns = [
    path('', panel.home, name="home"),

    path('file/', panel.local_file, name="local-file"),

    path('python/', Python.python, name="python"),

    path('server/commands/', Server.commands, name="commands"),
    path('server/commands/add/', Server.add_command, name="server-add-command"),
    path('server/commands/run/<id>', Server.run_command, name="server-run-command"),
    path('server/commands/pause/<id>', Server.stop_command, name="server-stop-command"),
    path('server/commands/delete/<id>', Server.delete_command, name="server-delete-command"),

    path('terminal/', Terminal.main, name="terminal"),
    path('terminal/getline/', Terminal.getline, name="terminal-getline"),
    path('terminal/reset/', Terminal.reset, name="terminal-reset"),

    path('forms/', Forms.main, name="forms"),
    path('forms/<int:id>', Forms.form, name="forms-form"),
    path('forms/<int:id>/<pk>', Forms.edit, name="forms-edit"),

    path('editor/', Editor.main, name="editor"),
    path('editor/delete/', Editor.delete, name="editor-delete"),
    path('editor/file/', Editor.file, name="editor-file"),
    
    path('settings/', panel.settings, name="settings"),
    
    path('users/', Users.main, name="users"),
    path('users/<id>', Users.user, name="users-user"),
    
    path('user/logout/<id>', panel.logout_user, name="logout-user"),
    path('user/login/', panel.login, name="login"),

    path('database/', Database.main, name="database"),
    path('database/<name>', Database.model, name="database-model"),
    path('database/<name>/add', Database.add, name="database-add"),
    path('database/<name>/<id>/edit', Database.edit, name="database-edit"),
    path('database/<name>/<id>/delete', Database.delete, name="database-delete"),
    path('database/<name>/<id>/show', Database.show, name="database-show"),
    
    path('messages/', Messages.main, name="messages"),
    path('messages/<id>', Messages.read, name="messages-read"),
    path('messages/send/<lang>', Messages.send, name="messages-send"),
    path('messages/readed/<id>', Messages.readed, name="messages-readed"),
    path('messages/remove/<id>', Messages.remove, name="messages-remove"),

    path('pages/', Pages.main, name="pages"),

    path('media/', Media.main, name="media"),
    path('media/images/', Media.images, name="media-images"),
    path('media/image/', Media.show_image, name="media-show-image"),
    path('media/videos/', Media.videos, name="media-videos"),
    path('media/audios/', Media.audios, name="media-audios"),
    path('media/copy/<type>/', Media.copy, name="media-copy"),
    path('media/cut/<type>/', Media.cut, name="media-cut"),

    path('charts/', Charts.main, name="charts"),

    path('languages/', Languages.main, name="languages"),


    re_path(r'^$', panel.error404)

]
