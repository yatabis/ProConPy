from setuptools import setup, find_packages


def requirements():
    with open("requirements.txt", 'r') as f:
        _requirements_list = [line.rstrip() for line in f]
    return _requirements_list


def readme():
    with open("README.md") as f:
        _readme_text = f.read()
    return _readme_text


setup(
    name='proconpy',
    version='0.0.1',
    description='Useful tools for participating in programming contests with Python.',
    long_description=readme(),
    author='yatabis',
    author_email='39yatabis.rim8820xxx@gmail.com',
    install_requires=requirements(),
    url='https://github.com/yatabis/ProConPy',
    license="MIT License",
    packages=find_packages(exclude=('tests', 'docs'))
)
