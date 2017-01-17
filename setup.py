from setuptools import setup

setup(
    name='shellphish-qemu',
    version='0.1',
    description="A pip-installable wrapper for qemu install.Based on v0.9.7 of shellphish-qemu",
    packages=['shellphish_qemu'],
    provides=['shellphish_qemu'],
    requires=['pkg_resources'],
    zip_safe=True,
    include_package_data=True,
    package_data={
        'shellphish_qemu': ['bin/*']
    }
)
