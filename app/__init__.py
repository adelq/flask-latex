from flask import Flask, Response
import urllib
import pexpect
from werkzeug import secure_filename
import uuid

# Create a Flask application with config
app = Flask(__name__)

PDFLATEX_COMMAND = "pdflatex -interaction=nonstopmode -output-directory=tex {}"

@app.route('/<path:url>')
def main(url):
    tex_uuid = uuid.uuid4()
    tex_filename = 'tex/{}'.format(str(tex_uuid))
    tex_file = urllib.urlretrieve(url, tex_filename)

    tex_render = pexpect.spawn(PDFLATEX_COMMAND.format(tex_filename))
    try:
        tex_render.expect("Output written on", timeout=30)
    except pexpect.TIMEOUT:
        return "Rendering the PDF took too long, please try again!"

    return Response(open(tex_filename+'.pdf'), mimetype='application/pdf')
