from setuptools import setup, find_packages

setup(
    name='easy_script',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        wlb=esp.cli:cli
    '''
)
