from setuptools import setup, find_packages

setup(
    name="tasty",
    version="0.1.0",
    author="AntispiralDisrespecter",
    description="A minimal functional language with terse lambda primitives",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AntispiralDisrespecter/tasty",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            'tasty=tasty.run:main',
        ],
    },
    include_package_data=True,
)
