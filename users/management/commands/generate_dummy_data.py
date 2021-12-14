from django.contrib.auth import get_user_model
from users.user_factory import (
    UserFactory,
)

from django.db import transaction
from django.core.management.base import BaseCommand


DEFAULT_NUM_OF_DATA = 7
NUM_USER = 100


class Command(BaseCommand):
    help = "Generates test data"

    def _delete_old_data(self):
        models = [
            get_user_model()
        ]
        
        self.stdout.write("Deleting old data...")
        for m in models:
            m.objects.all().delete()

    def _create_admin_users(self):
        self.stdout.write("Creating admin users...")
        # Default Users
        if not get_user_model().objects.filter(email__iexact='admin@admin.com').exists():
            u_admin = get_user_model()(email='admin@admin.com')
            u_admin.set_password("admin")
            u_admin.is_staff = True
            u_admin.is_superuser = True
            u_admin.save()

    def _create_new_data(self):
        self.stdout.write("Creating new data...")
        # users
        self._create_users_data()

    def _create_users_data(self):
        self.stdout.write("Creating users...")
        # Create all the users
        users = []
        for _ in range(NUM_USER):
            self.stdout.write(f"Creating user: {_ + 1}")
            user = UserFactory()
            users.append(user)

    @transaction.atomic
    def handle(self, *args, **kwargs):
        # delete old data
        self._delete_old_data()
        # create admin users
        self._create_admin_users()
        # create new data
        self._create_new_data()