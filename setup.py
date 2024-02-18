from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()
    
AUTHOR_NAME = 'Narius Bui'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup (
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    description = 'the first version of film recommendation system',
    long_description = description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS
)