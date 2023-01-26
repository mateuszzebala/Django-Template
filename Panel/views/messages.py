from Panel.utils import render
from Panel.models import Message
from django.shortcuts import redirect
from .panel import httpcode

class Messages:
    
    def main(request):
        if request.GET.get('readed') == 'true':
            messages = Message.objects.filter(readed=True)
        elif request.GET.get('readed') == 'false':
            messages = Message.objects.filter(readed=False)
        else:
            messages = Message.objects.all()
        return render(request, "Panel/Pages/messages/main.html", {"messages":messages})
    
    def send(request, lang):
        if request.method == "POST":
            msg = Message(
                email=request.POST.get('email'),
                content=request.POST.get('content'),
            )
            msg.save()
        request.COOKIES['form_sended'] = "true"
        return redirect("Main:page", name="index", lang=lang)
    
    def read(request, id):
        message = Message.objects.filter(id=id).first()
        if message is not None:
            return render(request, "Panel/Pages/messages/read.html", {"message":message})
        
    def readed(request, id):
        message = Message.objects.filter(id=id).first()
        message.readed = not message.readed
        message.save()
        return redirect("Panel:messages-read", id=id)
    
    def remove(request, id):
        message = Message.objects.filter(id=id).first()
        message.delete()
        return redirect("Panel:messages")
