**Описание Проекта**

**Django FreeIPA Auth** — это бэкэнд-приложение для аутентификации с простым решением для аварийного переключения сервера, которое можно включить в бэкенды аутентификации проекта. Это приложение взаимодействует с указанным хост-сервером FreeIPA и аутентифицирует пользователя в приложении django после успешного входа в систему freeIPA.


**Инструкция:**

1) Добавьте «freeipa_auth» в настройки INSTALLED_APPS следующим образом: 
```
INSTALLED_APPS = [
    ...
    'freeipa_auth',
]
```

2) Добавьте «freeipa_auth.backends.FreeIpaRpcAuthBackend» в AUTHENTICATION_BACKENDS в файле настроек следующим образом: 

```
AUTHENTICATION_BACKENDS = [
    ...
    'freeipa_auth.backends.FreeIpaRpcAuthBackend',
]
```
3) Добавьте в AUTH_USER_MODEL в файл настроек:
```
AUTH_USER_MODEL = 'freeipa_auth.ScUser'
```
4) Переопределите настройки в вашем файле настроек следующим образом: 
```
FREEIPA_AUTH_BACKEND_ENABLED = True
FREEIPA_AUTH_SERVER = ""  # по умолчанию None
FREEIPA_AUTH_FAILOVER_SERVER = None  # "ipa.failover.com" или по умолчанию None
FREEIPA_AUTH_SSL_VERIFY = False  # это будет путь к используемому сертификату ssl
FREEIPA_AUTH_UPDATE_USER_GROUPS = False  # по умолчанию False
FREEIPA_AUTH_UPDATE_USER_PERMISSIONS = False
FREEIPA_AUTH_USER_FLAGS_BY_GROUP = {
    "is_active": [""],
    "is_staff": [""],
    "is_superuser": [""]
}
FREEIPA_AUTH_ALWAYS_UPDATE_USER = True
FREEIPA_AUTH_USER_ATTRS_MAP = {
    "first_name": "givenname",
    "last_name": "sn",
    "email": "mail",
    'post': 'title',  # Должность
    'department': 'ou',  # Отдел
    'full_name': 'cn'  # ФИО
}
```
5) Создать и применить миграции: 
```
python3 manage.py makemigrations
python3 manage.py migrate
```
