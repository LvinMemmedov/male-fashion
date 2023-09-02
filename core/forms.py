



from django import forms
from core.models import Contact

class ContactFrom(forms.ModelForm):
    model=Contact 
    fields=['name', 'email', 'phone','message']