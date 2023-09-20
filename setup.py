from setuptools import setup, find_packages

setup(
    name='django_hypercurrent_middleware',
    version='1.11.0',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'hypercurrent_metering',  
    ],
    author='HyperCurrent, Inc',
    author_email='john.demic@hypercurrent.io',
    description='HyperCurrent Middleware for Python Django',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='Apache Software License',
    url='https://github.com/yourusername/django_hypercurrent_middleware',  # If you host your code on GitHub.
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)

