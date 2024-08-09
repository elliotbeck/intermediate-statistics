Here's how you can incorporate a section describing the usage of Poetry in your README:

---

# Intermediate Statistics

Welcome to the official repository for the Intermediate Statistics course
[03SM22MO0059](https://studentservices.uzh.ch/uzh/anonym/vvz/?sap-language=DE&sap-ui-language=DE#/details/2022/004/SM/51144599/50000003/Wirtschaftswissenschaftliche%2520Fakult%25C3%25A4t/50609459/Master%2520of%2520Science%2520UZH%2520in%2520Wirtschaftswissenschaften%2520(C%252C%2520PVO13)/51106318/Volkswirtschaftslehre%2520(Fast%2520Track)),
at the University of Zurich, Department of Economics. This repository contains all relevant Python code
used throughout the course.

## Table of Contents

- [About the Course](#about-the-course)
- [Installation](#installation)
- [Usage](#usage)
- [Using Poetry for Dependency Management](#using-poetry-for-dependency-management)
- [Note on Data](#note-on-data)
- [Contributing](#contributing)
- [License](#license)
- [Sources](#sources)

## About the Course

This repository is designed to accompany the Intermediate Statistics course offered at the University of Zurich, Department of Economics. It is intended to serve as a resource for students to access the code used in the course, with the aim of helping them better understand the statistical concepts discussed in lectures.

## Installation

Before you start, ensure you have Python installed on your machine. You will also need to install [Git LFS](https://git-lfs.com) to properly handle the files in this repository.

### Clone the Repository

To clone the repository, use the following command:

```bash
git lfs install
git clone https://github.com/yourusername/intermediate-statistics.git
```

## Usage

All the code in this repository is organized according to the course's weekly topics. Each directory corresponds to a specific lecture or assignment, containing the relevant Jupyter notebooks. You can run the code locally to replicate the analyses discussed in class.

Feel free to explore, modify, and run the code as needed to enhance your understanding of the material.

## Using Poetry for Dependency Management

This project utilizes [Poetry](https://python-poetry.org/) to manage dependencies and Python environments. Poetry simplifies the process of managing project dependencies, packaging, and versioning.

### Setting Up the Environment

To set up your environment using Poetry, follow these steps:

1. **Install Poetry**: If you haven't already, install Poetry by following the [official instructions](https://python-poetry.org/docs/#installation).

2. **Install Dependencies**: Navigate to the project directory and run:

    ```bash
    poetry install
    ```

    This command will create a virtual environment (if one doesn't exist) and install all required dependencies specified in the `pyproject.toml` file.

3. **Activate the Virtual Environment**: If you want to work within the Poetry-managed virtual environment, you can activate it by running:

    ```bash
    poetry shell
    ```

4. **Run Scripts or Notebooks**: You can now run any scripts or Jupyter notebooks within this environment.

### Adding or Updating Dependencies

To add a new package or update existing ones, use the following commands:

- **Add a Package**:

    ```bash
    poetry add <package_name>
    ```

- **Update Dependencies**:

    ```bash
    poetry update
    ```

Poetry will automatically update the `pyproject.toml` and `poetry.lock` files to reflect the changes.

### Exporting Dependencies

If you need to export the dependencies to a `requirements.txt` file (for compatibility reasons), you can do so with:

```bash
poetry export -f requirements.txt --output requirements.txt
```

This will generate a `requirements.txt` file based on the locked versions in `poetry.lock`.

## Note on Data

This repository includes some datasets to facilitate reproducibility and ease of access. Although including data directly in a repository is generally not recommended, Git LFS is used to manage these large files. Git LFS replaces large files with text pointers in the repository, while the actual file contents are stored on a remote server.

> **IMPORTANT:** Ensure that Git LFS is installed on your machine before cloning the repository.

## Contributing

Contributions are welcome! If you find any bugs or typos, please [open an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue), and I will address them as soon as possible. Even better, feel free to fork the repository and submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Sources

All code is authored by myself unless otherwise noted. Any external libraries or resources used are cited within the corresponding scripts or notebooks.
