from setuptools import setup, find_packages

setup(
    name='python-keylogger',
    version='1.0.0',
    description='A simple Python keylogger using pynput',
    author='Abdullah Javeid',
    author_email='your-email@example.com',
    url='https://github.com/AbdullahJaveid/python-keylogger',
    py_modules=['keylogger'],
    install_requires=[
        'pynput',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
