# SendGrid Email Sender

This script demonstrates how to use the SendGrid API to send an email from a Python script.

## Prerequisites

* A SendGrid account with an API key.
* Python 3 installed on your computer.

## Setup

Clone this repository to your computer.

* Install the required Python packages using pip:
* Create a .env file in the root directory of the project with the following content:

```
SENDGRID_API_KEY=your_api_key_here
```
Replace 'your_api_key_here' with your actual SendGrid API key.

## Creating and Activating a Virtual Environment

To ensure that the dependencies required by the script don't conflict with other Python packages installed on your system, you can create a virtual environment for this project.

Open a terminal or command prompt and navigate to the root directory of the project.

Run the following command to create a new virtual environment:

```
python -m venv env
```
This will create a new directory called env in the root directory of the project, containing a fresh installation of Python and pip.

Activate the virtual environment by running the appropriate command for your operating system:

* Windows: .\env\Scripts\activate.bat
* Mac/Linux: source env/bin/activate

You should see the name of the virtual environment appear in your command prompt or terminal prompt, indicating that you have successfully activated the virtual environment.

## Install the required packages using pip:
```
pip install -r requirements.txt
```
This will install the requests and python-dotenv packages required by the script.

The script will use the environment variables and packages installed in the virtual environment to send an email.

When you're finished using the script, you can deactivate the virtual environment by running the command deactivate in your terminal or command prompt.

## Running the Script

Run the script using the following command:
```
python emailscript.py
```
The script will use the API key from the .env file to send an email to the specified recipient.

## Notes

If you don't have a SendGrid account, you can sign up for free at https://sendgrid.com/free/

If you're having trouble getting the script to work, make sure that your API key is correct and that the required packages are installed.

You can also check the SendGrid API documentation for more information on how to use the API.