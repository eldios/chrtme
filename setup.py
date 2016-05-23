from distutils.core import setup

def main():
    setup_args = dict(
        name = "chrtme",
        packages = ["chrtme"],
        version = "0.0.5",
        license='MIT',
        description = "chroot wrapper and management utility",
        author = "Emanuele Lele Calo'",
        author_email = "lele<at>sshadm<dot>in",
        url = "https://github.com/eldios/chrtme.git",
        download_url = "https://github.com/eldios/chrtme/archive/master.zip",
        keywords = ["chroot","container","linux","rootfs"],
        classifiers = [
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Development Status :: 3 - Alpha",
            "License :: OSI Approved :: MIT License",
            "Operating System :: MacOS",
            "Operating System :: POSIX :: Linux",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: System :: Systems Administration"
            ],
        long_description = """\
chrtme - chroot wrapper and management utility
-------------------------------------

Simple tool to download, run and manage rootfs container-alike images in a dedicated chroot.

This version requires Python 3 or later.
"""
    )
    
    setup(**setup_args)

if __name__ == "__main__":
    main()
