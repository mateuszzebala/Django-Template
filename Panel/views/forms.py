from Panel.views.panel import httpcode
from Panel.utils import render
from Panel.views.panel import is_superuser
from Panel.config import registered_forms

class Forms:

    @is_superuser
    def main(request):

        return render(request, "Panel/Pages/forms/main.html", {
            "forms":registered_forms
        })

    @is_superuser
    def form(request, id):
        current_form = None
        try:
            current_form = registered_forms[id]
        except IndexError:
            return httpcode(request, 404, "Form doesn't exists")

        form = current_form['form'](request.POST or None)
        if form.is_valid():
            form.save()

        return render(request, "Panel/Pages/forms/form.html", {
            "form": current_form,
            "last_form": form,
        })

    @is_superuser
    def edit(request, id, pk):
        try:
            current_form = registered_forms[id]
        except IndexError:
            return httpcode(request, 404, "Form doesn't exists")
        item = current_form['model'].objects.filter(pk=pk).first()
        form = current_form['form'](request.POST or None, instance=item)
        if form.is_valid():
            form.save()
        current_form['form'] = form
        return render(request, "Panel/Pages/forms/form.html", {
            "form": current_form,
            "last_form": form,
        })



