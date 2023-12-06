from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

"""
class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, registro, password, **extra_fields):
        if not registro:
            raise ValueError('Seu registro é necessário!')
        user = self.model(registro = registro, username = registro, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, registro, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(registro, password, **extra_fields)
    
    def create_superuser(self, registro, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser needs the is_superuser=True')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser needs the is_staff=True')
        return self._create_user(registro, password, **extra_fields)
"""

class Post(models.Model):
    
    CATEGORIAS = [
        ['Biografia','Biografia'],
        ['Crônica','Crônica'],
        ['Drama','Drama'],
        ['Fábula','Fábula'],
        ['Fantasia','Fantasia'],
        ['Ficção científica','Ficção científica'],
        ['Horror','Horror'],
        ['Humor','Humor'],
        ['Infantil','Infantil'],
        ['Jornalismo literário','Jornalismo literário'],
        ['LGBT','LGBT'],
        ['Mistério','Mistério'],
        ['Mitologia','Mitologia'],
        ['Poesia','Poesia'],
        ['Policial','Policial'],
        ['Realismo mágico','Realismo mágico'],
        ['Relato de viagem','Relato de viagem'],
        ['Romance','Romance'],
        ['Romance de época','Romance de época'],
        ['Sátira','Sátira'],
        ['Suspense','Suspense'],
        ['Terror','Terror'],
    ]
    
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    conteudo = models.CharField(max_length=1000)
    estado = models.BooleanField()
    categorias = models.CharField(choices=CATEGORIAS, max_length=100)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.titulo
    
"""
class User(AbstractUser):
    registro = models.IntegerField(primary_key=True, unique=True)
    
    USERNAME_FIELD = 'registro'
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self):
        return str(self.registro)
    
    objects = CustomUserManager()
"""