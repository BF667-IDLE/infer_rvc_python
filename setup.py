import os
import platform
from setuptools import find_packages, setup

try:
    from pkg_resources import parse_requirements
except ImportError:
    # Fallback if pkg_resources is not available
    def parse_requirements(filename):
        """Load requirements from a pip requirements file."""
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]


setup(
    name="infer_rvc_python",
    version="1.2.0",
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

