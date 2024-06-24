from setuptools import setup

setup(
    name = "marquee",
    version = "1.0.0",
    packages = ["marquee"],
    install_requires = ["pygame"],
    entry_points = {
        "console_scripts" : "marquee = marquee.__main__:main"
    }

)