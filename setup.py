from setuptools import setup, find_packages

setup(
    name='tmux-run',
    version='0.0.1',
    description='Sends commands to tmux.',
    url='https://github.com/rshin/tmux-run',
    install_requires=['libtmux ~= 0.7.7'],
    extras_require={'dev': ['flake8 ~= 3.5.0', 'pre-commit ~= 1.4.4']},
    scripts=['tmux-run'], )
