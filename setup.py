from setuptools import setup

setup(
    name = 'bruttle',
    packages = ['bruttle'],
    version = '0.0.1',
    license = 'MIT',
    description = "A cli app to bruteforce pdf, zip, and some popular hashes",
    long_description = "Read docs at https://github.com/tamton-aquib/bruttle",
    author = 'aquib',
    author_email = 'aquibjavedt007@gmail.com',
    url = 'https://github.com/tamton-aquib/bruttle',
    keywords = ['bruteforce', 'pdf', 'zip', 'hash', 'cracking'],
    install_requires = [
        'pikepdf', 'tqdm'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        ],
    )
