from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authapp.models import User

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль!'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

class UserRegisterForm(UserCreationForm):
    pass