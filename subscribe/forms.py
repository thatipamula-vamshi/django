from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _


class SubscribeForm (forms.ModelForm):
    
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name':_('Enter the first name'),
            'last_name':_('Enter the last name'),
            'email':_('Email')
        }
        help_texts ={'first_name':_('Enter characters only')}
        error_messages = {
            'first_name':{
                'required':_('you cannot move forward without first name')
            }
        }


# def value_comma(value):
#     if ',' in value:
#         raise forms.ValidationError('Last name format is not Valid')

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField( max_length=100,required=False, )
#     last_name = forms.CharField( max_length=100,disabled=False, validators=(value_comma,))
#     email = forms.EmailField( max_length=100,help_text='Enter Gmail only with @',validators=())

    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if ',' in data:
    #         raise forms.ValidationError('Invalid format for Name')
    #     return data 