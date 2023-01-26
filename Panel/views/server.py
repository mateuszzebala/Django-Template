from django.shortcuts import redirect

from Panel.models import Command
from Panel.terminal import command
from Panel.utils import render
from Panel.views.panel import is_superuser


class Server:

    @is_superuser
    def commands(request):
        commands = Command.objects.all()
        temp = []
        for command in commands:
            temp.append({
                "id": command.id,
                "command": command,
                "run": command.is_run(),
                "name": command.name
            })
        commands = temp
        return render(request, "Panel/Pages/server.html", {
            "commands":commands,
        })
        
    @is_superuser
    def add_command(request):
        if request.method == "POST":
            cmd = request.POST.get("command")
            name = request.POST.get("name")
            cmd = Command(command=cmd, name=name)
            cmd.save()
        return redirect('Panel:server-commands')
    
    @is_superuser
    def run_command(request, id):
        cmd = Command.objects.filter(id=id).first()
        if not cmd.is_run():
            cmd.run()
        return redirect('Panel:server-commands')

    @is_superuser
    def stop_command(request, id):
        cmd = Command.objects.filter(id=id).first()
        if cmd.is_run():
            cmd.kill()
        return redirect('Panel:server-commands')

    @is_superuser
    def delete_command(request, id):
        cmd = Command.objects.filter(id=id).first()
        if cmd is not None:
            cmd.delete()
        return redirect('Panel:server-commands')
    
    
    

        
