from flask import Flask, request, render_template, redirect, url_for
from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename

import argparse
import cv2
import os
import hashlib
import numpy as np

from src import ImageDeepHash
from src import ImageDeepCompare


app = Flask(__name__, template_folder='templates', static_folder='static')

parser = argparse.ArgumentParser('Image Deep Hash')

parser.add_argument('--ngrok', action='store_true',
                    default=False, help="Run on local or ngrok")
parser.add_argument('--host',  type=str,
                    default='192.168.23.1:4000', help="Local IP")
parser.add_argument('--debug', action='store_true',
                    default=False, help="Run app in debug mode")

UPLOAD_FOLDER = './static/assets/uploads'
BLEND_FOLDER = './static/assets/blends'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['BLEND_FOLDER'] = BLEND_FOLDER

global m_hash, m_compare
m_hash = ImageDeepHash.ImageDeepHash()
m_compare = ImageDeepCompare.ImageDeepCompare()


@app.route('/')
def homepage():
    return render_template("hash.html")


@app.route('/compare')
def about_page():
    return render_template("compare.html")


@app.route('/analyze', methods=['POST', 'GET'])
def analyze():
    if request.method == 'POST':
        # Get input in form
        model_types = request.form.get('model-types')
        model_types = str(model_types)
        print("model: ", model_types)

        if 'compare-button' in request.form:
            f = request.files['file']
            f2 = request.files['file2']

            ori_file_name = secure_filename(f.filename)
            _, ext = os.path.splitext(ori_file_name)
            ori_file_name2 = secure_filename(f2.filename)
            _, ext2 = os.path.splitext(ori_file_name2)

            # Get cache name by hashing image
            data = f.read()
            print('ext: ', ext)
            filename = hashlib.sha256(data).hexdigest() + f'{ext}'

            data2 = f2.read()
            filename2 = hashlib.sha256(data2).hexdigest() + f'{ext2}'

            # save file to /static/uploads
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            np_img = np.fromstring(data, np.uint8)
            img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

            filepath2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
            np_img2 = np.fromstring(data2, np.uint8)
            img2 = cv2.imdecode(np_img2, cv2.IMREAD_COLOR)

            cv2.imwrite(filepath, img)
            cv2.imwrite(filepath2, img2)

            # Resize for blending 2 images
            img = cv2.resize(img, (480, 600))
            img2 = cv2.resize(img2, (480, 600))

            filename_blend = hashlib.sha256(data + data2).hexdigest() + '.jpg'
            filepath_blend = os.path.join(
                app.config['BLEND_FOLDER'], filename_blend)

            # Blending
            img_blend = cv2.addWeighted(img, 0.5, img2, 0.5, 0)

            cv2.imwrite(filepath_blend, img_blend)

            # Add compare image code here
            if model_types != 'VGG16':
                m_compare = ImageDeepCompare.ImageDeepCompare(
                    weight=model_types)

            metric_types = request.form.get('metric-types')
            metric_types = str(metric_types)
            print("metric: ", metric_types)
            compare_result = str(m_compare.compare(
                filepath, filepath2, metric_types))

            filename = os.path.basename(filename)
            filename2 = os.path.basename(filename2)
            filename_blend = os.path.basename(filename_blend)

            return render_template('analyze-compare.html', metric=metric_types, result=compare_result, fname=filename, fname2=filename2, fname_blend=filename_blend)

        if 'hash-button' in request.form:
            f = request.files['file']
            ori_file_name = secure_filename(f.filename)
            _, ext = os.path.splitext(ori_file_name)

            # Get cache name by hashing image
            data = f.read()
            filename = hashlib.sha256(data).hexdigest() + f'{ext}'

            # save file to /static/uploads
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            np_img = np.fromstring(data, np.uint8)
            img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
            cv2.imwrite(filepath, img)

            # Hashing
            hex_len = request.form.get('length-range')
            hex_len = int(hex_len)
            print("hex len: ", hex_len)

            if hex_len != 16 and model_types != 'VGG16':
                m_hash = ImageDeepHash.ImageDeepHash(
                    weight=model_types, hex_len=hex_len)

            m_hash.reset()
            m_hash.hash(filepath)
            hash_seq = m_hash.hexdigest()

            filename = os.path.basename(filename)

            return render_template('analyze-hash.html', hash_seq=hash_seq, fname=filename)

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
    if not os.path.exists(BLEND_FOLDER):
        os.makedirs(BLEND_FOLDER, exist_ok=True)

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

# python app.py --host localhost:8000
