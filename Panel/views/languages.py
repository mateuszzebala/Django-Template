
from Panel.views.panel import render
class Languages:
    def main(request):
        return render(request, 'Panel/Pages/languages/main.html')