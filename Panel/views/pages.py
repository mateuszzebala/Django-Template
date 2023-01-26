
from Panel.views.panel import render
class Pages:
    def main(request):
        return render(request, 'Panel/Pages/pages/main.html')