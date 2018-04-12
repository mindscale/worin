from setuptools import setup

setup(name='worin',
      version='0.0.2',
      description='A Korean POS Tagger using Neural Network',
      author='YU Jaemyoung',
      author_email='yu@mindscale.kr',
      url='https://github.com/mindscale/worin',
      packages=['worin'],
      package_data={
          '': ['*.txt', '*.md'],
          'worin': ['*.h5'],
      },
      install_requires=[
          'keras',
          'h5py',
      ],
      entry_points={
      },
      )
