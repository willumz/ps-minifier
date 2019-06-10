import setuptools

with open("README.md", "r") as f:
    longdesc = f.read()

setuptools.setup(
    name = "ps-minifier",
    version = "0.1.2",
    author = "Willumz",
    description = "A minifier for PowerShell scripts.",
    long_description = longdesc,
    long_description_content_type="text/markdown",
    url = "https://github.com/Willumz/ps-minifier",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    entry_points = {
        'console_scripts': ['psminifier=ps_minifier.psminifier:main']
    }
)