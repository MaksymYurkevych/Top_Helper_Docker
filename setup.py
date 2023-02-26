from setuptools import setup, find_namespace_packages

with open('README.md','r', encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name = 'Top-Helper-Bot',
    version = '1.1.4',
    description = 'Project "Personal Assistant" with a command line interface',
    url = 'https://github.com/Demonytro/Top-Helper-Bot.git',
    author = 'QUATTRO Team (Maria Savchuk, Maksym Yurkevych, Sviatoslav Butenko, Dmytro Oseledko)',
    long_description = long_description,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages = find_namespace_packages(),
    # install_requires = ["requests"],
    entry_points = {'console_scripts': ['topbot = top_helper_bot.menu:main_menu']}
)