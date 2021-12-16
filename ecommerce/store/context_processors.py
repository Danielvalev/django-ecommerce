from .models import Category


# This will allow categories to be accessible to every views, it need to be added to settings.py as well
def categories(request):
    return {
        'categories': Category.objects.all()
    }
