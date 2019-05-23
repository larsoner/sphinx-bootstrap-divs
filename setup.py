from setuptools import setup, find_packages

setup(
    name='sphinx-bootstrap-theme-collapse',
    version='1.0.0',
    url='https://github.com/larsoner/sphinx-bootstrap-theme-collapse.git',
    author='Eric Larson',
    author_email='larson.eric.d@gmail.com',
    description='Add a collapse directive for sphinx-bootstrap-theme',
    packages=find_packages(),
    install_requires=['sphinx', 'sphinx-bootstrap-theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={
        'sphinx-bootstrap-theme-collapse': ['collapse.js', 'collapse.css']},
)
