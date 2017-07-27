from setuptools import setup

__VERSION__ = "0.3.2.3"

setup(
    name='hangul-utils',
    version=__VERSION__,
    license="GPL",
    description='An integrated library for Korean preprocessing.',
    author='Kang Min Yoo',
    author_email='kaniblurous@gmail.com',
    url='https://github.com/kaniblu/hangul-utils',
    packages=['hangul_utils'],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: Korean",
        "Programming Language :: Java",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic"
    ],
    platforms=[
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    keywords=[
        "hangul-utils",
        "morphological analyzer",
        "morphology",
        "analyzer",
        "korean",
        "tokenizer",
        "sentence tokenizer",
        "word tokenizer",
        "pos tagger",
        "natural language processing",
        "jamo",
        "korean character",
    ],
    install_requires=[
        "tqdm",
        "six",
        "jpype1;python_version<='2.7'",
        "jpype1-py3;python_version>='3.5'",
        "mecab-python==0.996-ko-0.9.2"
    ],
    dependency_links=[
        "git+https://bitbucket.org/eunjeon/"
        "mecab-python-0.996#egg=mecab-python-0.996-ko-0.9.2"
    ]
)
