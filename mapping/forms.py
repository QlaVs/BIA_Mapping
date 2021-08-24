from django import forms
from .models import *


class UpdateUser(forms.ModelForm):

    def __init__(self, city_choices, ac_choices, nu_choices, *args, **kwargs):
        super(UpdateUser, self).__init__(*args, **kwargs)
        self.fields['city'].choices = city_choices
        self.fields['auto_column'].choices = ac_choices
        self.fields['user'].choices = nu_choices
    # local_list = []
    # for i in Cities.objects.filter().values():
    #     local_list.append((i['city_choice'], i['city_choice']))
    city = forms.ChoiceField()
    # local_list.clear()
    #
    # for i in AC.objects.filter().values():
    #     local_list.append((i['ac_choice'], i['ac_choice']))
    auto_column = forms.ChoiceField()
    # local_list.clear()
    #
    # for i in NewUser.objects.filter().values():
    #     local_list.append((i['nu_choice'], i['nu_choice']))
    user = forms.ChoiceField()
    # local_list.clear()

    class Meta:
        model = Users
        fields = ('city', 'auto_column', 'channel', 'epic', 'user')

# class MassRedact(forms.ModelForm):
#     class Meta:
#         model = Users
#         fields = ('city', 'auto_column', 'channel', 'user')


class MassRedact(forms.ModelForm):
    def __init__(self, redact_choices, *args, **kwargs):
        super(MassRedact, self).__init__(*args, **kwargs)
        self.fields['user'].choices = redact_choices

    user = forms.ChoiceField()

    class Meta:
        model = Users
        fields = ('user',)


class AddCity(forms.ModelForm):
    class Meta:
        model = Cities
        fields = ('city_choice',)


class AddAC(forms.ModelForm):
    class Meta:
        model = AC
        fields = ('ac_choice',)


class AddUser(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('nu_choice',)
