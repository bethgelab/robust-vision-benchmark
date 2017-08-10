from setuptools import setup
from setuptools import find_packages
from os.path import join, dirname
# We need io.open() (Python 3's default open) to specify file encodings
import io

with open(join(dirname(__file__), 'robust_vision_benchmark/VERSION')) as f:
    version = f.read().strip()

try:
    # obtain long description from README and CHANGES
    # Specify encoding to get a unicode type in Python 2 and a str in Python 3
    with io.open(
            join(dirname(__file__), 'README.rst'),
            'r',
            encoding='utf-8') as f:  # type: ignore
        README = f.read()
except IOError:
    README = ''

install_requires = [
    'bson',
    'flask',
    'foolbox',
    'numpy',
    'pillow',
    'requests',
    'setuptools',
]

tests_require = [
    'pytest',
    'pytest-cov',
]

setup(
    name="robust_vision_benchmark",
    version=version,
    description="An HTTP server and client that provides access to Foolbox models and attacks.",  # noqa: E501
    long_description=README,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="",
    author="Jonas Rauber & Wieland Brendel",
    author_email="opensource@bethgelab.org",
    url="https://github.com/bethgelab/robust-vision-benchmark",
    license="MIT",
    packages=find_packages(),
    scripts=[
        'bin/rvb-test-model',
        'bin/rvb-test-attack',
        'bin/rvb-upload'
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'testing': tests_require,
    },
)
