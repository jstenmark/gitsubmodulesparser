from setuptools import setup


def setup_package():
    setup(
        name="convert_gitmodules",
        version="0.0.1",
        author="Johannes Stenmark",
        description="A package for converting gitmodules",
        packages=["convert_gitmodules"],
        entry_points={
            "console_scripts": ["convert_gitmodules=convert_gitmodules.__main:main"]
        },
        install_requires=["argparse"],
    )


if __name__ == "__main__":
    setup_package()
