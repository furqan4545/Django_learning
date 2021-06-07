# so overhere we will create form and this time we will edit forms field with css classes as well. 
from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    # we need to connect this meta class to the model we r using.  and then we also wanna connect the field that we want to edit in this form. 
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')
        # let's add the widget.

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})  # so text widget is connected to 3 css classes. 
        }

    
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')
        # lets's add css classes to our form by defining widgets

        widgets = {
            'author': forms.TextInput(attrs= {'class': 'textinputclass'}),
            'text': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea'})
        }


