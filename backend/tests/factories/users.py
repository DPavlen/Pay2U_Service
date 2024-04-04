import factory
from users.models import MyUser

factory.Faker._DEFAULT_LOCALE = "en_US"


class UserFactory(factory.django.DjangoModelFactory):
    """User factory."""

    class Meta:
        """Factory configuration."""

        model = MyUser
        django_get_or_create = ("username",)

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    username = factory.Faker("user_name")
    full_name = factory.Faker("name")
    phone = factory.Faker("user_name")
    first_enter = True
    icon = factory.django.ImageField()
    role = MyUser.RoleChoises.USER
    password = factory.Faker("sha256")
