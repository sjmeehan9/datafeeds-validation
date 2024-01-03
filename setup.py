from setuptools import find_packages, setup

setup(name="datavalidation",
    version="1.0",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    install_requires=["pandas >= 2.0.3",
                      "PyYAML >= 6.0",
                      "matplotlib >= 3.8.0",
                      "pytest >= 7.4.4",
    ]
)