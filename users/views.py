
# Create your views here.
from django.views.generic import CreateView

from users.forms import UserCreateForm


class RegisterView(CreateView):
    form_class = UserCreateForm
    success_url = 'users/login/'
    template_name = 'users/user_create_form.html'
