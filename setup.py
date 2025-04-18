from setuptools import setup, find_packages

setup(
    name="balluff-llm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "datasets",
        "accelerate",
        "bitsandbytes",
        "peft",
        "scikit-learn",
        "pandas",
        "numpy",
    ],
    python_requires=">=3.8",
) 