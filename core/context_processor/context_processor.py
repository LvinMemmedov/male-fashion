
from core.models import Setting

def setting(request):
    setting = Setting.objects.first()
    context = {
        'setting': setting
    }
    return context