import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(name='pycrossva',
      version='0.93',
      description='prepare data from WHO and PHRMC instruments for verbal autopsy algorithms',
      url='https://github.com/verbal-autopsy-software/pyCrossVA',
      license='GNU General Public License v3.0',
      packages=find_packages(),
      entry_points='''
                    [console_scripts]
                    pycrossva-transform=pycrossva.scripts.pycrossva_transform:main
                    ''',
      include_package_data=True,
      package_data={
          'pycrossva': ['resources/mapping/*', 'resources/sample_data/*'],
      },
      keywords="verbal autopsy data preparation",
      install_requires=['numpy', 'pandas', 'Click'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: POSIX :: Linux",
      ],
      zip_safe=False,
)
