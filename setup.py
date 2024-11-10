from setuptools import setup, find_packages

setup(
    name='math_quiz',  # Replace with your project name
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here if you don't use requirements.txt
    ],
    include_package_data=True,
    description='A brief description of your project',
    long_description=open('C:/Users/z004nkac/OneDrive - Siemens AG/Desktop/DSSS_Temp/math_quiz/README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sayam-mad/math_quiz',  # Replace with your GitHub URL
    author='Sayam Das',
    author_email='sayamswapankrdas@gmail.com',
    license='MIT',  # Or another license
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
