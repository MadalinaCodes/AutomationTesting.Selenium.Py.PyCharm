The scope of this project is to test the some features from the https://demoqa.com/ site with the help of test scenarios.

#Prerequisites

To run this code, you need python 3.11, venv and pip to be installed.

	1. python 3.11
You need to have Python installed, at least the version 3.11 . Check if you already have Python installed running the Terminal command: python --version. If the result shows a version number, Python is already installed. If not, you can download it here: https://www.python.org/downloads/

	2. pip
pip is the package manager for Python. It is used to install and update packages in a virtual environment. Check if you have already pip installed running the Terminal command: pip --version. If the result shows a version number, pip is installed and there is no need for further actions. If not, instructions for downloading the latest version of pip can be found here: https://pip.pypa.io/en/stable/cli/pip_download/

	3. venv (Virtual Environment)
You need to create a virtual environment (venv) before running the application. For more information on how you create one, follow this link: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment

#Step 1 - I created an account 

For this, I went on the registering page https://demoqa.com/register, and I set some generic credentials in order to log on easily and they are already used in the code.

#Step 2 - Installation and Setup

I. I created a folder in my computer to store the code and run it.

II. The libraries used are selenium, behave and unittest. To install them, run the Terminal command:
	
	We install Selenium in order to interact with the browser
		pip install -U selenium

	Then we create a file named behave.ini and install Behave, which will help us interpret the project by creating html reports.
		pip install behave
		pip install behave-html-formatter
	
	We will also install the Gherkin and Ini pluggins, in order to create reports.
 
III. The browser.py file creates the Browser class and initializes the browser and waits.

In context.py file we have 2 methods, one that gets called before each test and another one which gets called after each test 

#Step 3 - Running the tests

In the test_runs folder we have some files that run the tests after the tags used in the project (@books, @regression, @smoke, @menu)​

All we have to do is right click on one of these runners and select run. After the test is done, a html report will be created or updated if it already exists

#Step 4 - Opening the report

After the report is done, it will appear under the reports folder, there, we can go and right click on it and select open in... whatever option we prefer. And we will see the result of the test.

