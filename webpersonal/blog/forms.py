from django.forms import ModelForm, forms
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name','content')
        labels = {
            'name': "Nombre",
            'content': "Contenido"
        }