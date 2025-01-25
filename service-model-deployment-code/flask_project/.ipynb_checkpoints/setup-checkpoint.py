from setuptools import setup, find_packages

setup(
    name='flask_project',                # Package name
    version='1.0.0',                     # Package version
    packages=find_packages(),            # Automatically find modules
    include_package_data=True,           # Include static and template files
    install_requires=[                   # Required dependencies
        'Flask',
        'numpy',
        'Pillow',
        'tensorflow'
    ],
    entry_points={
        'console_scripts': [
            'flask_project=flask_project.app:main',  # CLI command for the app
        ],
    },
)
