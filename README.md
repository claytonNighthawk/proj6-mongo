# proj6-mongo
Simple list of dated memos kept in MongoDB database

## What is here

A simple Flask app that displays all the dated memos it finds in a MongoDB database.
There is also a 'scaffolding' program, db_trial.py, for inserting a couple records into the database 
and printing them out.  Get db_trial.py working before you try making your flask app work. 

## What is not here

In addition to the missing functionality in the application, you will
need a MongoDB database, and you will need credentials (user name and
password) both for an administrative user and a regular user.  The
administrative user may be you, but the regular user is your
application. Make a subdirectory called "secrets" and place two files
in it: 

- secrets/admin_secrets.py holds configuration information for your MongoDB
  database, including the administrative password.  
- secrets/client_secrets.py holds configuration information for your
  application. 



## Functionality you'll add

The user should be able to add dated memos, either from the same index page or from a separate page. 
Memos should be displayed in date order. 
The user should be able to delete memos. 

## Setting up

Our use of the database is pretty simple, but you should anticipate
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


