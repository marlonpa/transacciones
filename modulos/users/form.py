from crispy_forms.layout import Submit, Button, Layout, Field, HTML, Row, Div
from django import forms
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError

from .models import Users
from django.contrib.auth.models import Group, Permission
from django.urls import reverse_lazy

url_tyc = reverse_lazy('users:ter_and_con')
url_reg_gru = reverse_lazy('users:reg_gru')
url_reg_tip_usu = reverse_lazy('users:reg_tip_usr')


#Form registrar usuario
class UsersForm(forms.ModelForm):
    def clean(self):
        dat_ide = self.cleaned_data.get("ide")
        if Users.objects.filter(ide=dat_ide).exists():
            c = Users.objects.get(ide=dat_ide)
            if self.instance.pk != c.pk:
                raise ValidationError("Ya existe el usuario")

    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'ide', 'email', 'is_active', 'is_admin', 'password', 'celular']

    def __init__(self, *args, **kwargs):
        super(UsersForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['ide'].required = True
        self.fields['email'].required = True
        self.fields['is_active'].required = False
        self.fields['is_admin'].required = False
        self.fields['password'].required = True
        self.fields['celular'].required = False
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_group_wrapper_class = 'row clearfix'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-10 col-md-10 col-sm-8 form-control-label'
        self.helper.field_class = 'col-lg-10 col-md-10 col-sm-8'
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-default'))
        self.helper.layout = Layout(
            'ide', 'first_name', 'last_name', 'email', 'celular', 'username',
            'password', 'is_admin', 'is_active'
        )


#Form actualizar usuario
class UusForm(forms.ModelForm):


    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'ide', 'email', 'is_active', 'is_admin', 'password', 'celular']

    def __init__(self, *args, **kwargs):
        super(UusForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['ide'].required = True
        self.fields['email'].required = True
        self.fields['is_active'].required = False
        self.fields['is_admin'].required = False
        self.fields['password'].required = True
        self.fields['celular'].required = False
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_group_wrapper_class = 'row clearfix'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-10 col-md-10 col-sm-8 form-control-label'
        self.helper.field_class = 'col-lg-10 col-md-10 col-sm-8'
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-default'))
        self.helper.layout = Layout(
            'ide', 'first_name', 'last_name', 'email', 'celular', 'username',
            'password', 'is_admin', 'is_active'
        )