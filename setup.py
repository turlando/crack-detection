from setuptools import setup

setup(
    name='crack-detection',
    version='0.0.1',
    url='',

    author='',
    author_email='',

    description='',
    long_description='',

    packages=['crack_detection'],

    entry_points={
        'console_scripts': [
            'crack-detection=crack_detection.__main__:main'
        ]
    },

    install_requires=[
        'numpy==1.21.5',
        'opencv-python==4.5.5.62',
        'opencv-contrib-python==4.5.5.62'
    ]
)
