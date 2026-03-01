import os
import platform
import pkg_resources
from setuptools import find_packages, setup

# Function to read requirements.txt
def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

setup(
    name="infer_rvc_python",
    version="1.0.0",
    description="Python wrapper for fast inference with rvc",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    readme="README.md",
    python_requires=">=3.10",
    author="R3gm",
    url="https://github.com/R3gm/infer_rvc_python",
    license="MIT",
    packages=find_packages(),
    package_data={'': ['*.txt', '*.rep', '*.pickle']},
    install_requires=parse_requirements('requirements.txt'),
    include_package_data=True,
    extras_require={"all": [
        "scipy",
        "numba==0.56.4",
        "edge-tts"
        ]},
)
