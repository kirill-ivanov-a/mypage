from setuptools import setup

setup(
    name='mypage',
    packages=['mypage'],
    include_package_data=True,
    install_requires=[
        'flask',
        'SQLAlchemy>=0.6',
    ],
)