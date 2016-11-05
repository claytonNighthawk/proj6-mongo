# proj6-mongo
Simple list of dated memos kept in MongoDB database

## What is here

A simple Flask app that displays all the dated memos it finds in a MongoDB database.
There is also a number of 'scaffolding' programs, such as db_trial.py, for inserting a couple records into the database 
and printing them out.  

## Testing

A suite of nose test cases is also included in this repo. They can be reached by `make test`.  

## What is not here

You will need a MongoDB database, and you will need credentials (user name and
password) both for an administrative user and a regular user.  The
administrative user may be you, but the regular user is your
application. Make a subdirectory called "secrets" and place two files
in it: 

- secrets/admin_secrets.py holds configuration information for your MongoDB
  database, including the administrative password.  
- secrets/client_secrets.py holds configuration information for your
  application. 


## Setting up

The use of the database is pretty simple, but you should anticipate
that installing MongoDB could take some time.  Since you may not be
able to install the same version of MongoDB on your development
computer and your Pi, it will be especially important to test your
project on the Pi. 

The version of MongoDB available for installing on Raspberry Pi with
apt-get is 2.4.  The version you can find for your development
computer is probably 3.x.  You may even have difficulty finding
documentation for 2.4, as it is considered obsolete.  However,
commands that work for 2.4 still seem to work for 3.x, so you should
write your application and support scripts to use 2.4.   The
difference that may cause you the most headaches is in creating
database user accounts (which are different than the Unix accounts for
users). 

In Python, the pymongo API works with both versions of MongoDB, so
it's only the initial setup where you have to be  
careful to use the right version-specific commands. 

### What do I need?  Where will it work? ###

* Designed for Unix, mostly interoperable on Linux (Ubuntu) or MacOS.
  Target environment is Raspberry Pi. 
  ** May also work on Windows (at least the W10 Ubuntu bash) or a Linux virtual machine
   out of the box depending on your pyvenv package command name. Program expects `make configure` to be run first but might require manual configuration by changing the PYVENV command name in templates.d/Makefile.standard between pyvenv and virtualenv. I could not get "pyvenv" to install on my pi or anywhere else but virtualenv worked everywhere.  

If you can run flask applications in your development environment, the
application would might be run by
`   python3 flask_main.py` or `make run`
and then reached with url
`   http://localhost:5000
