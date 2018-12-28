from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def create_user(self, form_data):
        self.create(
            first_name = (form_data['first_name']),
            last_name = (form_data['last_name']),
            email = (form_data['email'])
        )
    def delete_user(self, user_id):
        user = User.objects.get(id=user_id)
        user.delete()

    def update_user(self, form_data, user_id):
        b = User.objects.get(id=user_id)
        b.first_name = form_data['first_name']
        b.last_name = form_data['last_name']
        b.email = form_data['email']
        b.save()


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()
