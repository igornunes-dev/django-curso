from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

#criação
class CustomUserCreateForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ('first_name', 'last_name', 'phone')
    labels = {'username': 'Username/Email'}
  
  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    user.email = self.cleaned_data["username"]
    if commit:
      user.save()
    return user

#alteração
class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = ('first_name', 'last_name', 'phone')