from setuptools import setup,find_packages
import re
def version():
    filename = "MukeshAPI/__init__.py"
    with open(filename) as f:
        match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M)
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version
with open("README.md", encoding="utf8") as readme:
    long_desc = readme.read()
    


# Setting up
setup(
    name="MambaAPI",
    version=version(),
    author="Mamba | FantasticSukhi",
    author_email="itzcodermukesh@gmail.com",
    description="python api hub | MambaAPI",
    long_description_content_type="text/markdown",
    long_description=long_desc,
    packages=find_packages(),
    license="MIT",
    url="https://github.com/FantasticSukhi/MambaAPI",
    download_url="https://github.com/FantasticSukhi/MambaAPI/blob/main/README.md",
    install_requires=["pytz>=2023.3","requests-html","pillow","lxml_html_clean"],
    keywords=['python', "MambaAPI","flask"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    
    project_urls={
        "Tracker": "https://github.com/FantasticSukhi/MambaAPI/issues",
        "Community": "https://t.me/BLACKMAMBA_HU_VRO",
        "Source": "https://github.com/FantasticSukhi/MambaAPI",
    },
    python_requires="~=3.7",
)
