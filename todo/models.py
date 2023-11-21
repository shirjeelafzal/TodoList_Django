from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class MyManager(BaseUserManager):
    def create_user(self, email, name,view,edit, password=None,password2=None):
        """
        Creates and saves a User with the given email, name  and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            view=view,
            edit=edit
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,view,edit, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            view=view,
            edit=edit
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    view=models.BooleanField(default=False)
    edit=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name",'view','edit']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Task(models.Model):
    status_choices = [
        ("to_do", "to_do"),
        ("in_progress", "in_progress"),
        ("done", "done"),
    ]
    priority_choices = [
        ("low", "low"),
        ("medium", "medium"),
        ("high", "high"),
    ]
    name = models.CharField(max_length=15)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=status_choices, default="to_do")
    priority = models.CharField(max_length=15, choices=priority_choices, default="low")
    deadline = models.DateTimeField()
    start = models.DateTimeField()
    tag = models.CharField(max_length=15)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task2task', default=None)
    assigner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigners', default=None)

    def __str__(self):
        return self.name


class File(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['files', str(instance.task), filename])

    files = models.FileField(upload_to=nameFile, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return (str(self.task))


class History(models.Model):
    Desciption_change = models.TextField()
    time = models.DateTimeField()

    task = models.ForeignKey(Task, on_delete=models.CASCADE, default=None, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return (str(self.task))
