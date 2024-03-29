import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyhp",
    version="0.0.1",
    author="mehrab_cz",
    scripts=['pyhp/commands/pyhp'],
    # packages=['pyhp'],
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