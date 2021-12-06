from setuptools import setup

setup(
    name='nlppredtruecomparator',
    version='0.1.0',    
    description='A small tool to interactively compare prediction and ground truth in Jupyter for NLP tasks.',
    url='https://github.com/dddpt/nlp_pred_true_comparator',
    author='Didier Dupertuis',
    license='Apache License 2.0',
    packages=['nlppredtruecomparator_test'],
    install_requires=[
        'ipykernel>=6.4.1',
        'ipython>=7.28.0',
        'ipython-genutils>=0.2.0',
        'ipywidgets>=7.6.5',
        'jupyter>=1.0.0',
        'jupyter-client>=7.0.6',
        'jupyter-console>=6.4.0',
        'jupyter-core>=4.8.1',
        'jupyterlab-pygments>=0.1.2',
        'jupyterlab-widgets>=1.0.2'
    ],
    setup_requires=['wheel'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
