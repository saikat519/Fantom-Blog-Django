from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from .models import *
from crispy_forms import *

class PostCreationForm(forms.ModelForm):



    class Meta:
        model=Post
        widgets ={
            'title': forms.TextInput(attrs={'class':'single-input','placeholder':'Add your Post Title'}),
            'content': forms.Textarea(attrs={'class':'single-input','placeholder':'Add your Post Content'}),
        }



        fields=[
            'title',
            'category',
            'content',
            'image',
        ]


class PostUpdateForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(PostUpdateForm, self).__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method = 'post'
        self.helper.field_class = 'mt-10'
        self.helper.layout = Layout(
            Field("title",css_class="single-input",placeholder="Title"),
            Field("category",css_class="single-input",placeholder="Category"),
            Field("content",css_class="single-input",placeholder="Content"),
            Field("image",css_class="single-input"),
            Field("tag",css_class="single-input",placeholder="Your Tags",value=self.instance.post_tag()),
        )

        self.helper.add_input(Submit('submit','update',css_class="genric-btn success circle"))

    tag=forms.CharField()
    class Meta:
        model=Post
        fields=[
            'title',
            'category',
            'content',
            'image',
        ]



class CreateCommentForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(CreateCommentForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout=Layout(
            Field("name", css_class="form-control", placeholder="Name"),
            Field("email", css_class="form-control", placeholder="Email"),
            Field("content", css_class="form-control mb-10", placeholder="Content"),
        )
        self.helper.add_input(Submit('submit','Post Comment' ,css_class="primary-btn submit-btn"))



    class Meta:
        model=Comment
        fields=[
            'name',
            'email',
            'content'
        ]