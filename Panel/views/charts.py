
from Panel.views.panel import render
class Charts:
    def main(request):
        return render(request, 'Panel/Pages/charts/main.html')