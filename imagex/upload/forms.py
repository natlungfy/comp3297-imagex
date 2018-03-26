from django import forms
from .models import IMG



class SelectTestForm(forms.Form):
    city = forms.IntegerField(
        widget=forms.Select(
            choices=(
                (1, "BeiJing"),
                (2, "WeiHai"),
                (3, "RuShan"),
            ),
            attrs={
                "class": "form-control",
            }
        ),
        required=True
    )





        
       