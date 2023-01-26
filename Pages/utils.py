from .models import Language, Page


def get_page(language, page_name):

    language = Language.objects.filter(name=language).first()
    if language is None:
        return None

    page = Page.objects.filter(language=language, name=page_name).first()
    if page is not None and page.public:
        return page

    return None

