from setuptools import setup, find_packages

setup(
    name='TRACER',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List the dependencies of the TRACER package here
        albumentations==1.0.3,
        certifi==2022.12.7,
        colorama==0.4.4,
        cycler==0.10.0,
        imageio==2.9.0,
        joblib==1.2.0,
        kiwisolver==1.3.2,
        matplotlib==3.4.3,
        networkx==2.6.2,
        opencv-python-headless==4.5.3.56,
        Pillow>=9.0.0
        pyparsing==2.4.7,
        python-dateutil==2.8.2,
        PyWavelets==1.1.1,
        PyYAML==5.4.1,
        scikit-image==0.18.3,
        scikit-learn==0.24.2,
        scipy==1.7.1,
        six==1.16.0,
        sklearn==0.0,
        threadpoolctl==2.2.0,
        tifffile==2021.8.30,
        torch,
        torchvision,
        tqdm,
        wincertstore==0.2,
    ],
)