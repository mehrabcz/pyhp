import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyhp",
    version="0.0.1",
    author="mehrab_cz",
    entry_points = {
        # 'console_scripts': ['pyhp=funniest.command_line:main'],
        'console_scripts': ['pyhp=pyhp.py'],
    }

    author_email="babapourmehrab@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mehrabcz/pyhp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)