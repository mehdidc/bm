from setuptools import setup

setup(
    name="bm",
    version="0.1",
    author="mehdi cherti",
    author_email="mehdicherti@gmail.com",
    description=(""),
    license="MIT",
    keywords="",
    url="",
    zip_safe=False,  # the package can run out of an .egg file
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    platforms='any',
    scripts=['bm'],
    install_requires=['clize', 'bs4'],
)
