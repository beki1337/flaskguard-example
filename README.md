# FlaskGuard Example

This code is a simple demonstration of FlaskGuard, a library for Flask that provides request validation functionality.
Link to [git-repo](https://github.com/beki1337/FlaskGuard) and [pypi page](https://pypi.org/project/flask-guard/).

## Installation

To run this code, first ensure that you have Python installed on your system.
Then, make a new directory and navigate to it and create a virtual environment and activate it.
After that, clone the repository and navigate to the directory:
```bash
git clone https://github.com/beki1337/flaskguard-example.git
cd flaskguard-example
```

After that, install the necessary libraries:
```bash
pip install -r requirements.txt
```

## Usage 

To run the code, simply execute the app.py file:

```bash
python app.py
```

# Request Validation
FlaskGuard is used to validate requests to the /users and /messages endpoints. The validation rules are as follows:

/users: The request must have at least a 'name' key with a minimum length of 0 and maximum length of 20.
 It also needs to have an 'age' key with a value type of integer which has a minimum value of 0 and maximum value of 99 to be considered valid.
/messages: The request must have the 'message' key with a value of type string and a minimum length of 0 and a maximum length of 200 to be considered valid.
If a request fails validation, the server will return a 400 error along with a list of validation error messages.


