from setuptools import setup

setup(
    name='pytest-nice',
    version='0.1.0',
    description='A pytest plugin to turn Failure into Opportunity',
    url='https://<place this package introduced>',
    author='<your name>',
    author_email='<xxx@yyyy>',
    license='proprietrary',
    py_modules=['pytest'],
    install_requires=['pytest'],
    entry_points={'pytest11':['nice = pytest_nice',],},
)