from setuptools import setup, find_packages

name = 'sphinx-bootstrap-divs'
setup(
    name=name,
    version='1.0.0',
    url='https://github.com/larsoner/%s.git' % (name,),
    author='Eric Larson',
    author_email='larson.eric.d@gmail.com',
    description='Add div directives for sphinx-bootstrap-theme',
    packages=find_packages(),
    install_requires=['sphinx', 'sphinx-bootstrap-theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={name: ['bootstrap_divs.js', 'bootstrap_divs.css']},
)
