"""
Flask web app connects to Mongo database.
Keep a simple list of dated memoranda.

Representation conventions for dates: 
   - We use Arrow objects when we want to manipulate dates, but for all
     storage in database, in session or g objects, or anything else that
     needs a text representation, we use ISO date strings.  These sort in the
     order as arrow date objects, and they are easy to convert to and from
     arrow date objects.  (For display on screen, we use the 'humanize' filter
     below.) A time zone offset will 
   - User input/output is in local (to the server) time.  
"""

import flask
from flask import g
from flask import render_template
from flask import request
from flask import url_for

import json
import logging

# Date handling 
import arrow    # Replacement for datetime, based on moment.js
# import datetime # But we may still need time
from dateutil import tz  # For interpreting local times

# Mongo database
import pymongo
from pymongo import MongoClient
import secrets.admin_secrets
import secrets.client_secrets
MONGO_CLIENT_URL = "mongodb://{}:{}@localhost:{}/{}".format(
    secrets.client_secrets.db_user,
    secrets.client_secrets.db_user_pw,
    secrets.admin_secrets.port, 
    secrets.client_secrets.db)

###
# Globals
###
import CONFIG
app = flask.Flask(__name__)
app.secret_key = CONFIG.secret_key

####
# Database connection per server process
###

try: 
    dbclient = MongoClient(MONGO_CLIENT_URL)
    db = getattr(dbclient, secrets.client_secrets.db)
    collection = db.dated

except:
    print("Failure opening database.  Is Mongo running? Correct password?")
    sys.exit(1)


###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
  app.logger.debug("Main page entry")
  g.memos = get_memos()
  for memo in g.memos: 
      app.logger.debug("Memo: " + str(memo))
  return flask.render_template('index.html')


@app.route("/create")
def create():
    app.logger.debug("Create Page")
    return flask.render_template('create.html')


@app.route("/_submit", methods=["POST"])
def submit():
    app.logger.debug("Creating Memo")
    text = request.form["memo"]
    date = arrow.get(request.form["date"]).isoformat()
    memo = { "type": "dated_memo", 
           "date":  date,
           "text": text}

    app.logger.debug(memo)
    collection.insert(memo)
    return flask.render_template('create.html')

@app.route("/_delete_memo", methods=["POST"])
def delete_memo():
    app.logger.debug("Deleting Memo")
    memo_d_t = request.form["to_delete"].split(",")
    date = memo_d_t[0]
    text = memo_d_t[1]
    app.logger.debug(memo_d_t)
    collection.delete_one({"date": date, "text": text})
    g.memos = get_memos()
    for memo in g.memos: 
      app.logger.debug("Memo: " + str(memo))
    return flask.render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('page_not_found.html',
                                 badurl=request.base_url,
                                 linkback=url_for("index")), 404

#################
#
# Functions used within the templates
#
#################


@app.template_filter( 'humanize' )
def humanize_arrow_date( date ):
    """
    Date is internal UTC ISO format string.
    Output should be "today", "yesterday", "in 5 days", etc.
    Arrow will try to humanize down to the hour, so we
    need to catch 'today' as a special case. 
    """
    try:
        then = arrow.get(date).replace(tzinfo='local')
        now = arrow.now().floor('day')

        if then.date() == now.date():
            human = "Today"
        elif now.replace(days=+1).date() == then.date():
            human = "Tomorrow"
        elif now.replace(days=-1).date() == then.date():
            human = "Yesterday"    
        else: 
            human = then.humanize(now)

    except: 
        human = date
    return human


#############
#
# Functions available to the page code above
#
##############
def get_memos():
    """
    Returns all memos in the database, in a form that
    can be inserted directly in the 'session' object.
    """
    records = [ ]
    for record in collection.find({"type": "dated_memo"}).sort("date", -1):

        record['date'] = arrow.get(record['date']).isoformat()
        del record['_id']
        records.append(record)
    return records 


if __name__ == "__main__":
    app.debug=CONFIG.DEBUG
    app.logger.setLevel(logging.DEBUG)
    app.run(port=CONFIG.PORT,host="0.0.0.0")