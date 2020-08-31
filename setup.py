"""Project setup for `microspec-api`.

This is a project for installing the microspec package
independently of the microspeclib package.

I have no plans to publish this as a stand-alone. For public use,
the microspec package shall be bundled with microspeclib. For
initial development, it is easier to make it a separate project.

.. code-block:: bash

   git clone 
   cd microspec-api
   pip install -e .

"""
import setuptools

# Show PyPI.md as PyPI "Project description"
# encoding="utf-8" is for tree symbols: └─, ├─, etc.
with open("docs/PyPI.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="microspecapi", # do not use dashes or underscores in names!
    version="0.0.0", # must increment this to re-upload
    author="Chromation",
    author_email="mike@chromationspec.com",
    description="Chromation spectrometer dev-kit API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microspectrometer/microspec-api",
    project_urls={
        'Chromation': 'https://www.chromation.com/',
    },
    packages=setuptools.find_packages(),
    # Include `sdist` data files in the `bdist`.
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: User Interfaces",
    ],
    python_requires='>=3.7',
    install_requires=[
        "microspec"
        ],
    license='MIT', # field in *.egg-info/PKG-INFO
    platforms=['Windows', 'Mac', 'Linux'], # legacy field in *.egg-info/PKG-INFO
)


