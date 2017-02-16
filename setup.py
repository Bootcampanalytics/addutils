from distutils.core import setup
#import addutils

setup(name='AddUtils',
      version='1.1',
      description='Addfor tutorials visualization utilities',
      author='Daniele Trainini',
      author_email='daniele.trainini@add-for.com',
      package_data={'addutils': ['resources/*']},
      packages=['addutils'],
     )
