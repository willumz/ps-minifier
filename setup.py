import setuptools

with open("README.md", "r") as f:
    longdesc = f.read()

setuptools.setup(
    name = "ps-minifier",
    version = "0.1.1",
    author = "Willumz",
    description = "A minifier for PowerShell scripts.",
    long_description = longdesc,
    url = "https://github.com/Willumz/ps-minifier",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3"
    ],
    entry_points = {
        'console_scripts': ['psminifier=ps_minifier.psminifier:main']
    }
)