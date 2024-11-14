from django import forms
from users.models import CustomUser

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','first_name','last_name', 'gender', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        gender = user.gender
        if gender == 'male':
            user.profile_picture = 'profile_pictures/male.jpg'
        else:
            user.profile_picture = 'profile_pictures/male.png'
        user.save()
        return user

class UserLoginForm(forms.Form): 
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)

class ProfileForm(forms.ModelForm):
    class Meta:
        model= CustomUser
        fields =('username', 'email', 'first_name', 'last_name','profile_picture')

