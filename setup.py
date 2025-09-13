from setuptools import setup, find_packages

setup(
    name='EchoVerse',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A generative AI-based audiobook creation system that transforms user-provided text into expressive audio content.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/EchoVerse',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List the dependencies here, e.g.:
        # 'numpy',
        # 'pydub',
        # 'gTTS',
        # 'torch',
        # 'transformers',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)