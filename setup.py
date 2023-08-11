import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cancer-dash",
    version="0.0.1",
    author="Jamie Omondi",
    author_email="cruiseomondi90@gmail.com",
    description="A cancer dashboard built using streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",  # TODO
    packages=setuptools.find_packages(),
    classifiers=[],  # TODO
    requires=['streamlit', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'scikit-learn'],
    python_requires='>=3.6',
)
