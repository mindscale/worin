from distutils.core import setup

setup(name='worin',
      version='0.0.1',
      description='A Korean POS Tagger using Neural Network',
      author='YU Jaemyoung',
      author_email='yu@mindscale.kr',
      url='https://github.com/mindscale/worin',
      packages=['worin'],
      install_requires=[
          'keras',
          'h5py',
      ],
      entry_points={
      },
      )
