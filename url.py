import os
from PIL import Image
from flask import Flask, request, send_file
import urllib
import io
import re

app = Flask(__name__)
port = int(os.getenv("PORT", 4000))
thumbSize = 256, 256

def logMsg(args):
    print("[Instance: %s] %s" % (str(os.getenv("CF_INSTANCE_INDEX", 0)), args))

def getFileExt(url):
    rv = None
    m = re.match(r'^.+\.([^.]+)$', url)
    if m:
        rv = m.group(1)
    return rv

def getFileName(url):
    rv = None
    m = re.match(r'^.+/(.+?)\.[A-Za-z]{3,4}$', url)
    if m:
        rv = m.group(1)
    return rv

@app.route('/', methods=['POST', 'GET'])
def thumb():
    size = request.args.get('size')
    if size is None:
        size = thumbSize
    else:
        size = int(size), int(size)
    url = request.args.get('url')
    logMsg("Processing URL \"%s\" now ..." % url)

    # Replace cStringIO and StringIO with io
    img = Image.open(io.BytesIO(urllib.request.urlopen(url).read()))
    img.thumbnail(size)

    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

@app.route('/resize', methods=['POST'])
def resize():
    if 'file' not in request.files:
        return 'ERROR: no file present'

    file = request.files['file']
    size = request.form['size']

    if size is None:
        size = thumbSize
    else:
        logMsg("Got size: %s" % size)
        size = int(size), int(size)

    if file:
        logMsg("Got a file")
        img = Image.open(file)
        img.thumbnail(size)

        img_io = io.BytesIO()
        img.save(img_io, 'JPEG', quality=70)
        img_io.seek(0)

        return send_file(img_io, mimetype='image/jpeg')
    else:
        logMsg("No file")
        return 'Error: no image data present'

@app.route('/status')
def test():
    return "STATUS_OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True, debug=False)
