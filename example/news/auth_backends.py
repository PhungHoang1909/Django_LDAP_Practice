from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailDomainBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if not username.endswith('@company.vn'):
            return None
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except UserModel.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None
