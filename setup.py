from setuptools import find_packages, setup

setup(
    name='django-flat-responsive',
    packages=find_packages(),
    version=__import__('flat_responsive').__version__,
    author='elky',
    author_email='mail@elky.me',
    description=('An extension for Django admin that makes interface mobile friendly.'),
    license='BSD',
    url='https://github.com/elky/django-flat-responsive',
    download_url='https://github.com/elky/django-flat-responsive/tarball/1.2.0',
    keywords=['django', 'admin', 'responsive', 'mobile', 'interface'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
