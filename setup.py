from setuptools import find_packages, setup

_MAJOR               = 0
_MINOR               = 1
_MICRO = 5
version              = '%d.%d.%d' % (_MAJOR, _MINOR, _MICRO)
release              = '%d.%d' % (_MAJOR, _MINOR)

with open('README.md') as f:
    readme = f.read()


setup(
    name='simplepso',
    packages=find_packages(),
    version=version,
    description='Simple usage particle swarm optimization',
    author='James C. Pino',
    author_email='james.ch.pino@gmail.com',
    url='https://github.com/LoLab-VU/ParticleSwarmOptimization',
    keywords=['optimization',
              'systems biology'],
    classifiers=['License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2',],
    install_requires=['deap >= 1.0.2',
                      'matplotlib >= 1.5.0',
                      'numpy >= 1.11.0',
                      'scipy >= 0.17.1',
                      'pysb >= 1.1.1'],
    )
