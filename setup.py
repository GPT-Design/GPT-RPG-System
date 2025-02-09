from setuptools import setup, find_packages

setup(
    name="gpt_rpg",
    version="1.0.0",
    author="GPT-Design",
    author_email="your-email@example.com",
    description="An AI-driven modular RPG framework with emergent NPC behavior and world-building.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GPT-Design/GPT-RPG-System",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "rich",  # For better CLI display
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "gpt-rpg = gpt_rpg.main:main",
        ],
    },
)
