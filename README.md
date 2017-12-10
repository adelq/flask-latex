LaTeX as a Service
==================

*Render LaTeX files on the web into PDF!*

This LaTeX rendering service is used to run [ViewTex](https://chrome.google.com/webstore/detail/viewtex/hndddfcnkkjfkjmhnofcalgjheifajac),
previously known as [Chrome LaTeX](https://github.com/pbjr23/chrome-latex), ChromeTeX, or TeXChrome.

The production service is now defunct due to server costs, but this app server
works just as well as it did in 2014 when written originally.

## Installation

This is a simple [Flask](http://flask.pocoo.org/) web application. To install, you must have Python,
git, and pip installed. It is recommended to install these dependencies inside a
virtualenv.

```
pip install -r requirements.txt
python run.py
```

However, for the application to run as intended, you must install the TeX suite
of applications, preferably with `texlive-full` in order to render as many
documents as fully as possible. Without the full package, you may encounter
difficulties rendering documents with obscure packages, citation styles, fonts,
etc.

## Usage

`flask-latex` has a single simple endpoint to render the LaTeX file at the
provided URL and returns a PDF.

**URL:** `/<path>`

**Method:** `GET`

**Success Response:** HTTP Status Code 200, mimetype `application/pdf`

**Sample Call**

```
wget http://localhost:5000/http://www.shivkumar.org/research/papers/erica/newerica6.tex
```

TODO
----
* Allow for configurable number of compiles
