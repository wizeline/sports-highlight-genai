from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sports-highlight-genai",
    version="0.1.0",
    author="Fabián Portillo, Narda Ballesteros, Jose Hialgo, Fernanda Meza",
    author_email="fabian.portillo@wizeline.com, jose.hidalgo@wizeline.com, narda.ballesteros@wizeline.com, luisa.meza@wizeline.com",
    description="Develop a GenAI-powered tool that automatically identifies key moments in sports events to generate highlight reels. This project leverages real-time statistical data, video processing, and image analysis to create engaging sports highlights. Optional features include video editing capabilities and social media integration for sharing highlights.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wizeline/sports-highlight-genai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "boto3==1.24.28",
        "requests==2.32.2",
        "flask==2.1.3",
        "python-dotenv==0.19.2",
        "gunicorn==20.1.0",
        "pytest==7.1.2",
    ],
    entry_points={
        'console_scripts': [
            'sports-highlight-genai=src.app:main',
        ],
    },
)
