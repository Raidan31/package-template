from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Image Processing",
    version="0.0.1",
    author="Raidan Nunes de Oliveira",
    author_email="raidan.nunes31@gmail.com",
    description="Pacote de Processamento de Imagem",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Raidan31/package-template.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)