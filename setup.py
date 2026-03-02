import os
import re
from setuptools import find_packages, setup

def parse_requirements(filename):
    """Load requirements from a pip requirements file, handling Git URLs."""
    with open(filename, 'r') as file:
        lines = []
        for line in file:
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            
            # Handle Git URLs (convert to PEP 508 direct reference format)
            if line.startswith('git+') or ('github.com' in line and line.startswith('http')):
                # Extract package name from the URL
                # Example: git+https://github.com/BF667-IDLE/fairseq.git -> fairseq
                match = re.search(r'/([^/]+?)(?:\.git)?$', line)
                if match:
                    pkg_name = match.group(1)
                    # Convert to PEP 508 format: package_name @ git+url
                    lines.append(f"{pkg_name} @ {line}")
                else:
                    # Fallback: add #egg=package_name if we can't parse it
                    # This is less ideal but may work with older pip
                    lines.append(line)
            else:
                lines.append(line)
        
        return lines

# Read long description from README.md
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="infer_rvc_python",
    version="1.2.0",
    description="Python wrapper for fast inference with rvc",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.10",
    author="R3gm",
    url="https://github.com/R3gm/infer_rvc_python",
    license="MIT",
    packages=find_packages(),
    package_data={'': ['*.txt', '*.rep', '*.pickle']},
    install_requires=parse_requirements('requirements.txt'),
    include_package_data=True,
    extras_require={
        "all": [
            "scipy",
            "numba==0.56.4",
            "edge-tts"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
            )
