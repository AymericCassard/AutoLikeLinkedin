Cd to the root of project
Build Project:

python -m build

(If build is not installed):

pip install --upgrade build

Activate the venv(unix):

source ./bin/activate

Build Selenium dependencies:

pip install -r requirements.txt

Enter your Linkedin credentials in ./src/credentials.py

Run project:

python ./src/main.py