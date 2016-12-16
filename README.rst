Django Flat Responsive
======================

Description
-----------

**django-flat-responsive** is an extension for Django admin and
`django-flat-theme <https://github.com/elky/django-flat-theme/>`_.
This app adds CSS file which contains specific media queries for
mobile devices, such as phones and tablets.


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


Important note
--------------
⚠️ If you have your own custom ``base_site.html`` file, you need to add the following lines to it to make this app work:

::

     {% load admin_static %}
     {% block blockbots %}
       {{ block.super }}
       <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">
       <link rel="stylesheet" type="text/css" href="{% static 'admin/css/responsive.css' %}" />
     {% endblock %}


Compatibility
-------------

Works in modern mobile browsers which support `CSS Flexbox <http://caniuse.com/#search=flexbox>`_.


Testing
-------

Tested with:

|4|


Guaranteed works in:

- iOS Safari 7+
- Android Browser 4.4+
- Chrome for iOS 30+
- Chrome for Android 30+
- Firefox for iOS 5.0+
- Firefox for Android 50+
- Windows Phone IE Mobile 11+

If you found any issues or want this app to support other browser versions -
please report `here <https://github.com/elky/django-flat-responsive/issues/>`_.


Screenshots
-----------

**Login page**

|1|

------------

**Dashboard**

|2|

------------

**Calendar widget**

|3|

.. |1| image:: https://cloud.githubusercontent.com/assets/209663/20430873/f001c6ee-adea-11e6-9695-df9957db09ce.png
.. |2| image:: https://cloud.githubusercontent.com/assets/209663/20430878/f72836ce-adea-11e6-8517-ef6d2fddd241.png
.. |3| image:: https://cloud.githubusercontent.com/assets/209663/20430883/fee78e00-adea-11e6-9bcb-8cac5a314094.png
.. |4| image:: http://elky.me/browserstack.svg
   :width: 200px
   :target: http://browserstack.com/
