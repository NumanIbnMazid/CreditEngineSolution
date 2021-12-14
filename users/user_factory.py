from django.contrib.auth import get_user_model
import factory
from factory.django import DjangoModelFactory


# *** User ***

class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('email',)

    name = factory.Faker("first_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall('set_password', 'test12345')
