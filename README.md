<div id="top"></div>
<!-- PROJECT SHIELDS -->
<!--
*** See the bottom of this document for the declaration of the reference variables
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/GEOSYS">
    <img src="https://earthdailyagro.com/wp-content/uploads/2022/01/Logo.svg" alt="Logo" width="400" height="200">
  </a>

  <h1 align="center"> Analytic processor template</h1>

  <p align="center">
    Learn how to use &lt&geosys/&gt platform capabilities in your own business workflow! Build your processor and learn how to run them on your platform.
    <br />
    <a href="https://earthdailyagro.com/"><strong>Who we are</strong></a>
    <br />
    <br />
    <a href="https://github.com/GEOSYS/GeosysPy/issues">Report Bug</a>
    ·
    <a href="https://github.com/GEOSYS/GeosysPy/issues">Request Feature</a>
  </p>
</p>

<div align="center">
</div>

<div align="center">

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url]
[![Youtube][youtube-shield]][youtube-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

</div>

<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  <ol>
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  * [Prerequisite](#prerequisite)
  * [Installation](#installation)
- [Usage](#usage)
  * [Run the example inside a Docker container](#run-the-example-inside-a-docker-container)
  * [Usage with Jupyter Notebook](#usage-with-jupyter-notebook)
- [Project Organization](#project-organization)
- [Resources](#resources)
- [Support development](#support-development)
- [License](#license)
- [Contact](#contact)
- [Copyrights](#copyrights)
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<p> The aim of this project is to help our customers valuing &ltgeosys/&gt platform capabilities to build their own analytic of interest. </p>

This repository contains template files based on the cookiecutter system, which allows to rapidly create basic folder structure for data science projects at EarthDaily Agro.

When using the `cookiecutter` command on this repository, it creates a git repository, folders and files structure populated with some of the information provided by the user.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisite

To be able to run this example, you will need to have following tools to be installed



1. Install Git

    Please install Git on your computer. You can download and install it by visiting the [official Git website]    (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and following the provided instructions

2. Install Conda

    Please install Conda on your computer. You can download and install it by following the instructions provided on the [official Conda website](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

3. Install Python 
    Python 3.7+

4. Install cookiecutter
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```



Make sure you have valid credentials. If you need to get trial access, please register [here](https://earthdailyagro.com/geosys-api/#get-started).



This package has been tested on Python 3.9.7.

<p align="right">(<a href="#top">back to top</a>)</p>



## Usage

### start using the template

To create your repo using this template, perform these steps : 


1. Call the template:

    You can directly call this template from github using the following command : 

    
   ```
     cookiecutter https://github.com/GEOSYS/analytic-processor-template
   ```

   Or you can call it after cloning the analytic template repo locally : 

   ```
    git clone cookiecutter https://github.com/GEOSYS/analytic-processor-template
    cookiecutter <local_path_to>/analytic-processor-template
   ```
    
2. You will be prompted for the following informations to initialize the project:

 - `project_name` : Readable name of the project or technology, e.g. Machine Learning based Time Series Classification
 - `project_repo` : the name of the created repository of the project, default to e.g. machine-learning-based-time-series-classification
 - `project_slug` : "slug" of the project, default to e.g. machine_learning_based_time_series_classification
 - `author_name` : the name of the authors
 - `description` : "A short description of the project.",
 - `python_interpreter` : ["python3", "python"]

<!-- PROJECT ORGANIZATION -->
## Project Organization
      {{ cookiecutter.project_repo }}
       ├── README.md          <- The top-level README for developers using this project.
       ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
       │                         the creator's initials, and a short `-` delimited description, e.g.
       │                         `1.0-jqp-initial-data-exploration`.
       │
       ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
       │                         generated with `pip freeze > requirements.txt`
       ├── environment.yml    <- The conda requirements file for reproducing the analysis environment, e.g.
       │                         generated with `conda env export > environment.yml`, or manually
       │
       ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
       ├───src                <- Source code for use in tis project.
       │   ├───main.py 
       │   ├───api
       │   │   ├── __init__.py
       │   │   └── api.py
       │   └───{{ cookiecutter.project_slug }}
       │       ├── __init__.py
       │       └── {{ cookiecutter.project_slug }}.py
       └── tests 

<p align="right">(<a href="#top">back to top</a>)</p>


## Linking your repo to github

Using cookiecutter creates the folders locally, but you may want to version control it. Here are the steps :

 - Create a new repository, without adding any source to it (.gitignore and README.md files will be created by cookiecutter)
 - go to the created project folder, and run:
   - `git init`
   - `git add *`
   - `git commit -m "first commit"`
   - (modify first) `git remote add origin <yourorganisationgit>/<repo>.git`
   - `git push -u origin main`
   
### Customization

You can modify the template according to your liking and needs

1. Clone the project repository:

    ```
    git clone https://github.com/GEOSYS/analytic-processor-template
    ```


2. Change the cookiecutter.json:

      You can enter any template parameter you want to use. 


3. Directly add or delete folders and files.

   You can then use the new template using the same commands as before.



<p align="right">(<a href="#top">back to top</a>)</p>





<!-- RESOURCES -->
## Resources 
The following links will provide access to more information:
- [EarthDaily agro developer portal  ](https://developer.geosys.com/)
- [Pypi package](https://pypi.org/project/geosyspy/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Support development

If this project has been useful, that it helped you or your business to save precious time, don't hesitate to give it a star.

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the [GPL 3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html). 

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

For any additonal information, please [email us](mailto:sales@earthdailyagro.com).

<p align="right">(<a href="#top">back to top</a>)</p>

## Copyrights

© 2022 Geosys Holdings ULC, an Antarctica Capital portfolio company | All Rights Reserved.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- List of available shields https://shields.io/category/license -->
<!-- List of available shields https://simpleicons.org/ -->
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- List of available shields https://shields.io/category/license -->
<!-- List of available shields https://simpleicons.org/ -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=social
[NETcore-shield]: https://img.shields.io/badge/.NET%20Core-6.0-green
[NETcore-url]: https://github.com/dotnet/core
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=plastic&logo=appveyor
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/analytic-processor-template/repo.svg?style=plastic&logo=appveyor
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/GEOSYS/analytic-processor-template/repo.svg?style=social
[issues-url]: https://github.com/GEOSYS/analytic-processor-template/issues
[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg
[license-url]: https://opensource.org/licenses/MIT
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=social&logo=linkedin
[linkedin-url]: https://www.linkedin.com/company/earthdailyagro/mycompany/
[twitter-shield]: https://img.shields.io/twitter/follow/EarthDailyAgro?style=social
[twitter-url]: https://img.shields.io/twitter/follow/EarthDailyAgro?style=social
[youtube-shield]: https://img.shields.io/youtube/channel/views/UCy4X-hM2xRK3oyC_xYKSG_g?style=social
[youtube-url]: https://img.shields.io/youtube/channel/views/UCy4X-hM2xRK3oyC_xYKSG_g?style=social
[language-python-shiedl]: https://img.shields.io/badge/python-3.9-green?logo=python
[language-python-url]: https://pypi.org/ 
[GitStars-shield]: https://img.shields.io/github/stars/GEOSYS?style=social
[GitStars-url]: https://img.shields.io/github/stars/GEOSYS?style=social
[CITest-shield]: https://img.shields.io/github/workflow/status/GEOSYS/analytic-processor-template/Continous%20Integration
[CITest-url]: https://img.shields.io/github/workflow/status/GEOSYS/analytic-processor-template/Continous%20Integration






