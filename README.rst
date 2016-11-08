Django Flat Responsive
======================

Description
-----------

**django-flat-responsive** is an extension for Django admin and
`django-flat-theme <https://github.com/elky/django-flat-theme/>`_ that makes
interface good for mobile and tablets. This app adds CSS file which contains
specific media queries for mobile devices.

Installation
------------

Install via pip:
``pip install django-flat-responsive``

**For Django 1.9+**

Put ``flat_responsive`` app in your *INSTALLED\_APPS* **before**
``django.contrib.admin``:

 ::

     INSTALLED_APPS = (
         ...
         'flat_responsive',
         'django.contrib.admin',
         ...
     )


**For older Django versions**

If you use Django version older than 1.9 this app will work properly only
in pair with `django-flat-theme <https://github.com/elky/django-flat-theme/>`_.
Put ``flat_responsive`` app in your *INSTALLED\_APPS* **before** ``flat``:

 ::

     INSTALLED_APPS = (
         ...
         'flat_responsive',
         'flat',
         'django.contrib.admin',
         ...
     )


Compatibility
~~~~~~~~~~~~~

Works in modern mobile browsers which support `CSS Flxebox <http://caniuse.com/#search=flexbox>`_.


Testing
~~~~~~~

Tested in:

- iOS Safari 9+
- Android Browser 4.4
- Chrome for iOS 53
- Chrome for Android 53

If you found any issues or want this app to support other browser versions -
please report `here <https://github.com/elky/django-flat-responsive/issues/>`_.
