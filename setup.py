from setuptools import setup


with open("README.md", "rt") as fp:
    DESCRIPTION = fp.read()


if __name__ == "__main__":
    setup(
        name="import_profiler",
        version="0.0.4.dev",
        author="David Cournapeau",
        author_email="cournape@gmail.com",
        license="MIT",
        install_requires=["attrs >= 17.1.0", "tabulate >= 0.7.5"],
        description="Import profiler to find bottlenecks in import times.",
        long_description=DESCRIPTION,
        py_modules=["import_profiler"],
    )
