"""
https://packaging.python.org/tutorials/packaging-projects/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dataterkinigempabumidiindoensia",
    version="0.1",
    author="Syamsul Arifin",
    author_email="syamsularifin18@gmail.com",
    description="This package will get the latest earthquake indonesia from BMKG | Meteorology Climatology and "
                "Geophysics Agency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/syamsularifin18/latest-indonesia-earthquake",
    project_urls={
        "website": "https://remotework.id",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "src"},
    #packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
