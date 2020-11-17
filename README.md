## Persona Galleria

## Author
 [Bethwel Kiplimo](https://github.com/bethwelkip)


* Link to live site
https://persona-galleria.herokuapp.com

## Description
This website allows a user to view my displayed photos, they can also choose to view the photos based on the photo's location.
they can then search for categories of photos. The user is free to copy and share the link to an image.

# Live Site 
If you are only interested in viewing the deployed web app, click on the link below:
**[Persona-Galleria](https://persona-galleria.herokuapp.com)**


## Installation Requirements
  If you would like to look at or toy around further with the source code, follow the following steps:
  * Clone this repository and navigate to the folder: git clone https://github.com/bethwelkip/Persona_Galleria.git

  Once in the folder, open your terminal and run the following commands to set up your working environment:-
  * sudo pip install python3.7
  * python3.7 -m venv virtual
  * conda deactivate
  * source virtual/bin/activate
  * pip install -r requirements.txt (installs all necessary dependencies)
  * configure your database by navigation to settings.py and find the database settings and then rename the "Name" and "Password" and "Host" to thos of your local machine. 
   The application is now ready to be served.
   Run the following in your terminal  to serve the application
* python manage.py runserver

 
## User Stories
  * A user can see the photos posted by the admin
  * A user can search for the different categories of photos
  * A user can view photos based on the set location

## Technologies Used
  * Python3.7
  * HTML5, Bootstrap
  * Django
  * PostgreSQL
  * Heroku

## Known Bugs
No known bugs so far but if any is found, please let me know at bkiplimo@princeton.edu

## LICENSE
Licenced under [MIT LICENSE](LICENSE)