import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "text_summarization"
AUTHOR_USER_NAME = "manthrishivaji"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "2019mmb1320@iitrpr.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = "AUTHOR_EMAIL",
    description = "A small python package for NLP app",
    lon_description = long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where='src')
)