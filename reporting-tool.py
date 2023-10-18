# app.py
import os
from flask import Flask, render_template
from nbconvert import HTMLExporter

app = Flask(__name__)

@app.route('/')
def report():
    # Convert the Jupyter Notebook to HTML
    notebook_path = 'report.ipynb'
    exporter = HTMLExporter()
    output, resources = exporter.from_filename(notebook_path)

    return render_template('report.html', report=output)

if __name__ == '__main__':
    app.run(debug=True)
