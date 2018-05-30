from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pyautomailer',
      version='0.1.1-dev',
      description='A fully customizable automatic bulk email sending script.',
      long_description=readme(),
      classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Topic :: Communications :: Email',
            'Natural Language :: English',
            'Operating System :: Microsoft :: Windows'
          ],
      keywords='automatic email service',
      url='https://github.com/matteocappello94/pyautomailer',
      author='Matteo Cappello',
      author_email='matteocappello94@gmail.com',
      license='MIT',
      packages=['pyautomailer'],
      zip_safe=False,
      entry_points = {
              'console_scripts': ['pyautomailer=pyautomailer.command_line:main']
          },
      test_suite='nose.collector',
      tests_require=['nose'])
