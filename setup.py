from setuptools import setup, find_packages

setup(
    name='ml123',
    version='0.2',
    description='A package with short ML programs',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'seaborn',
        'matplotlib',
        'scikit-learn',
    ],
)
