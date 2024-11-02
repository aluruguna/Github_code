from django import forms
from .models import Post

class SearchForm(forms.Form):
    query = forms.CharField()


class TestForm(forms.Form):
    text = forms.CharField(min_length=7)
    boolean = forms.BooleanField()
    integer = forms.IntegerField()
    email = forms.EmailField()

    def clean_integer(self):
        integer = self.cleaned_data.get("integer")
        if integer <10:
            raise forms.validationError("This integer is less than 10")
        return self.cleaned_data


class AnotherForm(forms.Form):
    RADIO_CHOICES = [
        ('signin', 'Sign In'),
        ('signup', 'Sign Up'),
        ('forgotpassword', 'Forget Password')
    ]

    CHECKBOX_CHOICES = [
        ('terms','Agree to terms and conditions'),
        ('privacy','Agree to privacy policy'),
       
    ]

    INT_CHOICES = [tuple([x,x]) for x in range(0, 100)]

    text = forms.CharField(label="Feedback", min_length=7, widget=forms.Textarea)
    integer = forms.IntegerField(initial =10, widget = forms.Select(choices=INT_CHOICES))
    radio_choices = forms.CharField(min_length=7,widget=forms.RadioSelect(choices=RADIO_CHOICES))
    checkbox_choices = forms.CharField(min_length=7,widget=forms.CheckboxSelectMultiple(choices=CHECKBOX_CHOICES)) 

class PostModelForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields= ["user","title","slug","image","content","draft","publish"]
        exclude= []
 
