# Smart-Power-IoT
ELEN4009 Smart Home Power Management (Project 18) - Ari Croock, Kanaka Babshet. Alice Yang, Daniel Weinberg

The project uses the Django web application framework with a SQLite database.

`smart_home` is the root Django project directory.
Within `smart_home`, the directory `smart_home` contains the website configuration, and `devices` contains the application source code.

## How to setup the application
It is recommended that you setup and use a Python virtual environment to run the application. For details, please see [Creation of virtual environments](https://docs.python.org/3/library/venv.html) or Google.

Do the following in order to setup the web application for use (you only need to do this once):

1. Make sure you have Python version 3.4+ and pip functioning correctly
2. Clone the project repository
3. Install the project dependencies by running `pip install -r requirements.txt` in the root project directory.
4. Change directory to the `smart_home` directory that contains `manage.py` and apply the database migrations by running `python manage.py migrate`
5. Create an admin user by running `python manage.py createsuperuser` and entering your desired username and password
6. In order to start the server, run `python manage.py runserver`. This will start the server listening on localhost port 8000. The system setup is now complete.

## How to use the application
1. After you have started the server, go to [http://localhost:8000/](http://localhost:8000/) in your favourite web browser, click on `Admin` in the navbar and login.
2. To add a new device, click on `Add` next to `Devices` under the heading `DEVICES`
3. Fill out out the form with the details of your device. In order to add a new `Location` click on the `+` next to the `Location` drop-down menu, enter a name and click `SAVE`. Click `SAVE` to save your device. Do this for each device you would like to manage.
4. Now go back to [http://localhost:8000/](http://localhost:8000/) to access the main website. From here, you can see the list of devices and toggle their states on and off. To view details for all devices, click on `All Device Information`. To view details for only a specific device, click on that device's title.

