# Repository Name - Sphinx Documentation Sample

Welcome to the SampleDocumentationPDF repository! This documentation is a part of my portfolio as a technical writer and was created using the RestructuredText (reStructuredText) language. The documentation showcases my skills in writing technical content and using tools like Sphinx and simplePDF package to generate PDF files.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

In this repository, you will find the documentation for the project that I worked on as a technical writer. The documentation is written in reStructuredText, a lightweight markup language, and generated using Sphinx, a powerful documentation generation tool. The main goal of this project is to showcase my abilities as a technical writer, demonstrating my skills in writing clear, concise, and well-structured technical documentation.

## Getting Started

To access and use the documentation, you have two options:

1. **Viewing Online**: You can view the documentation online by navigating to the pdf file `String Manipulation for Technical Writers Documentation.pdf`

2. **Local Setup**: To set up the documentation locally on your machine, please follow the instructions below:

### Installation

To install and build the documentation locally, you'll need to have the following tools installed:

- Python (version 3.9 or higher)
- pip package manager

Once you have the required tools, follow these steps:

1. Clone this repository to your local machine.

```
git clone https://github.com/anna-niezychowska/SampleDocumentationPDF.git
cd SampleDocumentationPDF
```

2. Install the necessary dependencies.

```
pip install -r requirements.txt
```

### Usage

After completing the installation, you can now build the documentation using Sphinx and generate a PDF file using the simplePDF package. To build the documentation, run the following command:

```
sphinx-build -b html source/ build/
```

The generated HTML documentation can be accessed by opening the `index.html` file located in the `build/` directory with your web browser.

If you prefer to generate a PDF version of the documentation, use the following command:

```
sphinx-build -b pdf source/ pdf/
```

The PDF file will be available in the `pdf/` directory.

Feel free to explore the different sections of the documentation to understand the project, its features, and how to use it effectively.

## Contributing

As this repository is a part of my portfolio, I am not actively accepting contributions. However, I welcome any feedback or suggestions you may have. If you find any issues or have ideas for improvement, please feel free to open an issue in the repository.

## License

The content in this repository is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the content following the terms of the license.

---

Thank you for visiting this repository and exploring the documentation. If you have any questions or need further assistance, please don't hesitate to reach out to me via annaniezychowska1407@gmail.com. I hope you find this documentation informative and well-structured.

Happy documenting!
