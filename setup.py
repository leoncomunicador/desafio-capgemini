from setuptools import setup

setup(
    name="desafio_capgemini",
    description="Deasfio Capgemini",
    install_requires=["pypubsub==4.0.3"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
