from flask import Flask, flash, url_for
from flask import render_template, make_response
from flask import request, redirect, send_from_directory
from flask_mail import Mail, Message
import os
import nestautils as nu


BASE_APP_PATH       = 'http://nestanmr.com'
DOCS_URL            = 'http://docs.nestanmr.com'
#BASE_APP_PATH       = 'http://45.63.14.213:8080'
#DOCS_URL            = 'http://45.63.14.213:8081'

MAIL_SERVER         = 'x'
DEFAULT_MAIL_SENDER = 'x'
MAIL_PORT           = 465
MAIL_USE_SSL        = True
MAIL_USERNAME       = 'x'
MAIL_PASSWORD       = 'x'

BASE_DOWNLOAD_PATH  = os.sep.join([BASE_APP_PATH,'static'])
BASE_LINK_PATH      = os.sep.join([BASE_APP_PATH,'download'])
LOGFILE_PATH        = 'submissions.csv'
PUSHOVER_NOTIFY     = False

SOFTWARE_DIRECTORY  = 'software'
NESTANMR_PATH       = os.sep.join([SOFTWARE_DIRECTORY, nu.get_nestanmr_latest_version(SOFTWARE_DIRECTORY)])

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = ''
mail = Mail(app)




def send_download_link(email, name, link, sender):
    
    # Generate message content
    subject = 'Download link for NESTA-NMR'
    body = 'Greetings %s,\n\nNESTA-NMR can be downloaded at %s.\n\n'%(name, link) + \
    'This link will be active for approximately 24 hours.\n\nPlease note that this email address is not monitored.\n\nThank you.\n'
    
    # Create the message
    msg = Message(subject, recipients=[email])
    msg.sender = sender
    msg.body = body

    # Send the message
    try:
        mail.send(msg)
    except:
        sender = 'admin2@nestanmr.com'
        msg.sender = sender
        try:
            mail.send(msg)
        except:
            try:
                send_notification("NESTAWEB Failed Email: "+email)
            except:
                pass
    return sender


@app.route('/')
def index():
    return render_template('index.html',invalid_form=False,message='',docsurl=DOCS_URL)


@app.route('/signup', methods = ['POST'])
def signup():
    nesta_address = app.config['BASE_APP_PATH']

    name = request.form['name'].strip()
    email = request.form['email'].strip().lower()
    institution = request.form['institution'].strip()

    trusted_proxies = {'127.0.0.1'}
    route = request.access_route + [request.remote_addr]
    ipaddress = next((addr for addr in reversed(route) 
                    if addr not in trusted_proxies), request.remote_addr)

    if ((name=='')|(email=='')|(institution=='')):
        message = 'Name, email address, and institution are required.'
        return render_template('index.html', invalid_form=True, message=message)

    else:
        
        link = nu.create_download_link(source=app.config['NESTANMR_PATH'], directory='static', nesta_link_path=app.config['BASE_LINK_PATH'])

        admin_email = send_download_link(email, name, link, app.config['DEFAULT_MAIL_SENDER'])

        print("Name %s Email %s Institution %s IP address %s"%(name, email, institution, ipaddress))

        return render_template('success.html', email=email, name=name, admin_email=admin_email)


@app.route('/download/<code>')
def render_download_page(code, nesta_dl_path=app.config['BASE_DOWNLOAD_PATH'], source=app.config['NESTANMR_PATH']):
    # Get the file size
    filesize = str(int(os.path.getsize(os.sep.join(['.',source])) >> 20))

    # Split up the source file path
    filename = os.path.split(source)[-1]
    (basename, extension) = os.path.splitext(filename)
    download_link = os.sep.join([nesta_dl_path, basename + '_' + code + extension])
    return render_template('download.html', download_link=download_link, filesize=filesize)


@app.route('/manual')
def show_pdf(directory='static'):
    return redirect('/static/NESTANMR_Manual.pdf')


@app.route('/robots.txt')
def for_robots():
    return redirect('/static/robots.txt')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
    #app.run(host='127.0.0.1', debug=True)
    #app.run(host='0.0.0.0', debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True)


