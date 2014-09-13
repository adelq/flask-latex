from flask import Flask, Response
import urllib
import pexpect
import uuid
import os

# Create a Flask application with config
app = Flask(__name__)

PDFLATEX_COMMAND = "pdflatex -interaction=nonstopmode -output-directory=tex {}"

@app.route('/<path:url>')
def main(url):
    print "Hello world 1"
    # Generate UUID for each file uploaded
    tex_uuid = uuid.uuid4()
    tex_filename = 'tex/{}'.format(str(tex_uuid))
    urllib.urlretrieve(url, tex_filename)

    print "Hello world 2"
    # Try to render LaTeX to PDF
    tex_render = pexpect.spawn(PDFLATEX_COMMAND.format(tex_filename))
    try:
        tex_render.expect("Output written on", timeout=30)
    except pexpect.TIMEOUT:
        return "Rendering the PDF took too long, please try again!"

    print "Hello world 3"
    # Load PDF into memory
    pdf_filename = tex_filename + '.pdf'
    pdf_file = open(pdf_filename)

    print "Hello world 4"
    # Remove files from filesystem
    os.remove(tex_filename)
    os.remove(pdf_filename)
    os.remove(tex_filename+'.aux')
    os.remove(tex_filename+'.log')

    print "Hello world 5"
    return Response(pdf_file, mimetype='application/pdf')
