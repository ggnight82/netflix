
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self,email,username,rating,first_name,last_name,password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            rating=rating,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password,rating,first_name,last_name):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            rating=rating,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    RATING = (
        ('1','All'),
        ('2', '7+'),
        ('3', '12+'),
        ('4', '15+'),
        ('5','Rated-R'),
        ('6','19+')
    )
    id =                models.BigAutoField(help_text="User Id", primary_key=True)
    email =             models.EmailField(verbose_name='email', max_length=60, unique=True)
    username =          models.CharField(max_length=30, unique=True)
    date_joined =       models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login =        models.DateField(verbose_name='last login', auto_now=True)
    is_admin =          models.BooleanField(default=False)
    is_active =         models.BooleanField(default=True)
    is_staff =          models.BooleanField(default=False)
    is_superuser =      models.BooleanField(default=False)
    rating =            models.CharField(max_length=1,choices=RATING)
    first_name =        models.CharField(verbose_name='first_name', max_length=30)
    last_name =         models.CharField(verbose_name='last_name', max_length=30)

    REQUIRED_FIELDS = ['username','first_name','last_name','rating']
    USERNAME_FIELD = 'email' 

    objects = MyUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
