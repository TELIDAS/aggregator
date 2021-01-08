from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class UserCreateForm(UserCreationForm):
    """
    Form for user sighup
    """
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'age',
            'username',
        ]