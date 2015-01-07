#!/usr/bin/python2.7

import cherrypy
import os
import jinja2
import re

import smtplib
from email.mime.text import MIMEText

APP_PATH = os.path.dirname(os.path.abspath(__file__))
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=APP_PATH+"/templates"))

    
class ApplicationForm(object):
    def index(self):
        t = env.get_template("application_form.html")
        return t.render({"nav": "application_form"})

    index.exposed = True

class Root(object):
    application_form = ApplicationForm()

    def index(self):
        t = env.get_template('index.html')
        return t.render({"nav": "home"})

    index.exposed = True

if __name__ == "__main__":
    print APP_PATH
    conf = {
        "/":{"tools.staticdir.root": APP_PATH
            ,"tools.sessions.on": True
            }
        ,"/static":{"tools.staticdir.on":True
                    ,"tools.staticdir.dir":"static/"
                    }
        ,"/favicon.ico":{"tools.staticfile.on":True
                        ,"tools.staticfile.filename":APP_PATH+"/static/images/logo/favicon.ico"
                        }
    }
    print conf['/']
    print conf['/static']
    cherrypy.quickstart(Root(), '/', config=conf)
else:
    cherrypy.config.update({'environment': 'embedded'})
    application = cherrypy.Application(Root(), script_name=None, config=None)

