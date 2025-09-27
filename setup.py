from setuptools import setup, find_packages

setup(
    name="jwt-security-analyser",
    version="0.1.0",
    description="A tool for analyzing JWT tokens for security vulnerabilities and best practices.",
    author="Allsafecybertech",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PyJWT>=2.0.0"
    ],
    entry_points={
        "console_scripts": [
            "jwt-security-analyser=jwt_security_analyser.analyser:main",
        ],
    },
    python_requires=">=3.7",
    license="MIT",
)