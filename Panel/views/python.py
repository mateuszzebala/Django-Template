from Panel.terminal import command
from Panel.utils import render
from Panel.views.panel import is_superuser


class Python:
    @is_superuser
    def python(request):
        if request.method == "POST":
            code = request.POST.get("python-code")
            if code is not None:
                with open("Panel/temp/python_code.py", "w") as file:
                    file.write(code)
                cmd = command("python python_code.py", "Panel/temp", True)
                cmd = "\n".join(cmd)
                return render(request, "Panel/Pages/python.html", {
                    "console_content": cmd,
                    "code": code
                })

        return render(request, "Panel/Pages/python.html")
