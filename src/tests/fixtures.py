import pytest


@pytest.fixture
def create_user(django_user_model):
    def make_user(**kwargs):
        """
        Create and return a custom user
        with email='test@test.test' and pass='test1234' as default.
        """
        kwargs["password"] = "test1234"
        if "email" not in kwargs:
            kwargs["email"] = "test@test.test"
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def user(create_user):
    """Create and return a default custom user."""
    return create_user()


@pytest.fixture
def admin_user(create_user):
    """Create and return a default admin custom user."""
    return create_user(is_staff=True, is_superuser=True)
