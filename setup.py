from setuptools import setup, find_packages

setup(
    name="IDS706_7_PyPackage",  # package name
    version="0.1",
    # packages=find_packages(),  # automatically find packages
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'run_main=main:main',  # Invoke the main function in main.py by running the command run_main
        ],
    },
    install_requires=[  # specify the dependencies
        'pandas',
        'python-dotenv',
        'databricks',
    ],
    include_package_data=True,
    description="A Python package for Haobo's IDS706_7_PyPackage project",
    author="Haobo Yuan",
    author_email="haobo.yuan@duke.edu",
    url="https://github.com/haobo-yuan/IDS706-7-PyPackage",
)
