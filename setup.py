from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='unicov',
  version='0.0.1',
  description='Universal File conversion python library to convert any file to any type of file',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/SwarajJalkote/csv_to_dat',  
  author='Swaraj Jalkote',
  author_email='swarajjalkote98@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  py_modules=['unicov'],
  package_dir={'':'src'},
  keywords=['csv', 'dat', 'xml', 'json', 'parquet', 'avro', 'excel', 'type', 'file', 'convertor'], 
  install_requires=['setuptools', 'pandas'] 
)