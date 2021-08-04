from flask import Flask, request, render_template, redirect, url_for
from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename

import argparse
import cv2
import os
import hashlib
import numpy as np


app = Flask(__name__, template_folder='templates', static_folder='static')

parser = argparse.ArgumentParser('Image Deep Hash')

parser.add_argument('--ngrok', action='store_true',
                    default=False, help="Run on local or ngrok")
parser.add_argument('--host',  type=str,
                    default='192.168.23.1:4000', help="Local IP")
parser.add_argument('--debug', action='store_true',
                    default=False, help="Run app in debug mode")

UPLOAD_FOLDER = './static/assets/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/analyze', methods=['POST', 'GET'])
def analyze():
    if request.method == 'POST':
        if 'upload-button' in request.form:
            f = request.files['file']
            ori_file_name = secure_filename(f.filename)
            _, ext = os.path.splitext(ori_file_name)

            # Get cache name by hashing image
            data = f.read()
            filename = hashlib.md5(data).hexdigest() + f'{ext}'

            # save file to /static/uploads
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            np_img = np.fromstring(data, np.uint8)
            img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
            cv2.imwrite(filepath, img)

            # Add some code here ...
            hash_seq = "0x82e7adf01f96f8f373e0c3caaa9a414a"

        filename = os.path.basename(filename)
        print('Filename: ', filename)
        return render_template('analyze.html', hash_seq=hash_seq, fname=filename)

    return redirect('/')


@app.after_request
def add_header(response):
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'public, no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
    return response


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    args = parser.parse_args()

    if args.ngrok:
        run_with_ngrok(app)
        app.run()

    else:
        hostname = str.split(args.host, ':')
        if len(hostname) == 1:
            port = 4000
        else:
            port = hostname[1]
        host = hostname[0]
        app.run(host=host, port=port, debug=args.debug, use_reloader=False)
