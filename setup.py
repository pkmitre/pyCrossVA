from setuptools import setup

setup(name='pycrossva',
      version='0.4a9',
      description='prepare data from WHO and PHRMC instruments for verbal autopsy algorithms',
      url='https://github.com/verbal-autopsy-software/pyCrossVA',
      license='GNU General Public License v3.0',
      packages=['pycrossva'],
      entry_points='''
                    [console_scripts]
                    pycrossva-transform=pycrossva.scripts.pycrossva_transform:main
                    ''',
      include_package_data=True,
      keywords="verbal autopsy data preparation",
      install_requires=['numpy', 'pandas', 'Click'],
      zip_safe=False)
