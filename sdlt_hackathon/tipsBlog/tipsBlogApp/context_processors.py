from .models import Category

def menuitems(request):
  return {
    'category_menu': Category.objects.all()
  }