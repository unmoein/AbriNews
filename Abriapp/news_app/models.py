from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, mobile_number, password=None, **extra_fields):
        if not mobile_number:
            raise ValueError('The Mobile Number must be set')
        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', User.Roles.SUPER_USER)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(mobile_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        SUPER_USER = 'SUPER_USER', 'Super User'
        ADMIN = 'ADMIN', 'Admin'
        REGISTERED_USER = 'REGISTERED_USER', 'Registered User'
    
    mobile_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.REGISTERED_USER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.mobile_number
    
class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.news}'

class Like(models.Model):
    news = models.ForeignKey(News, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('news', 'user')

