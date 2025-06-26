import nox


@nox.session
def lint(session):
    session.install(
        'pytest>=5.3.5',
        'setuptools>=45.2',
        'wheel>=0.34.2',
        'flake8>=3.7.9',
        'numpy==2.1.3',
        'pandas==2.2.2',
    )
    session.install('.')
    session.run('flake8', 'sklearn_pandas/', 'tests')


@nox.session
@nox.parametrize('numpy', ['2.1.3'])
@nox.parametrize('scipy', ['1.13.1'])
@nox.parametrize('pandas', ['2.2.2'])
def tests(session, numpy, scipy, pandas):
    session.install(
        'pytest>=5.3.5',
        'setuptools>=45.2',
        'wheel>=0.34.2',
        f'numpy=={numpy}',
        f'scipy=={scipy}',
        f'pandas=={pandas}',
    )
    session.install('.')
    session.run('py.test', 'README.rst', 'tests')
