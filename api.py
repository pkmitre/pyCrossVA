# Put a simple API in front of pyCrossVA
# Note: this currently takes CSV and returns CSV, JSON may eventually be preferred

import sys
from io import StringIO
from flask import Flask, jsonify, request
import pandas as pd
from pycrossva.transform import transform

app = Flask(__name__)

@app.route('/transform', methods=['POST'])
def transform_route():

  # Read the input and output formats from the query string
  input_format = request.args.get('input')
  output_format = request.args.get('output')

  # Read the CSV from the body of the request
  csv = request.data.decode("utf-8")
  data = pd.read_csv(StringIO(csv))

  # Run the transform and return the result in CSV
  result = transform((input_format, output_format), data)
  return result.to_csv()
