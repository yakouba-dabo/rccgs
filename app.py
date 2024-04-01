from flask import Flask, render_template, request, flash, redirect, url_for, session, abort, jsonify, send_file, send_from_directory
import os
import requests
import time

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)





app.config["DEBUG"] = True


app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')



@app.route('/')
def home():
    return send_from_directory('template', 'index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    try:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            con = request.form['message']


            msg = Message('You Are Booked', sender = 'olamicreas@gmail.com', recipients = ['salemrockent@gmail.com'] )
            msg.html = "<div style='padding:15px; height:100%; width:100%'>{}<hr> Reply to the sender's mail {}</div>".format(con, email)
            
            mail.send(msg)
            return render_template('contact.html')
    except:
        flash("Unkown error occured, try again")
       
        return redirect('/')
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/pastor')
def pastor():
    return render_template('pastor.html')

@app.route('/pod')
def podcast():
    return render_template('pod.html')

@app.route('/pr')
def pr():
    return render_template('pr.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/donate')
def donate():
    return render_template('donate')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/choir')
def choir():
    return render_template('choir.html')

@app.route('/location')
def lacation():
    return render_template('location.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/sunday')
def sunday():
    return render_template('sunday.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/values')
def values():
    return render_template('values.html')

@app.route('/vid')
def vid():
    return render_template('vid.html')


@app.route('/ytlive')
def ytlive():
    return render_template('ytlive.html')


@app.route('/prreq')
def prreq():
    return render_template('prreq.html')

@app.route('/bible')
def bible():
    return render_template('bible.html')




if __name__ == '__main__':
    app.run()
