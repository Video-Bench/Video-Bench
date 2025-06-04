#!/usr/bin/env python

from setuptools import find_packages, setup
import os

def fetch_readme():
    with open('README.md', encoding='utf-8') as f:
        text = f.read()
    return text

def fetch_requirements():
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
    with open(filename, 'r') as f:
        envs = [line.rstrip('\n') for line in f.readlines() if '@' not in line]
    return envs

install_requires = fetch_requirements()
setup(name='videobench',
      version='0.1.2',
      description='Human Preference Aligned Video Generation Benchmark',
      long_description=fetch_readme(),
      long_description_content_type='text/markdown',
      project_urls={
          'Source': 'https://github.com/Video-Bench/Video-Bench',
      },
      entry_points={
          'console_scripts': ['videobench=videobench.cli.evaluate:main']
      },
      install_requires=install_requires,
      packages=find_packages(),
      include_package_data=True
)
