# Put a simple API in front of pyCrossVA
# Note: this currently takes CSV and returns CSV, JSON may eventually be preferred

from io import StringIO
from flask import Flask, request
import pandas as pd
from pycrossva.transform import transform
from pycrossva.utils import detect_format

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


@app.route('/detect_format', methods=['POST'])
def detect_format_route():

  # Read the CSV from the body of the request
  csv = request.data.decode("utf-8")
  data = pd.read_csv(StringIO(csv))

  # Read the threshold input parameter (if specified)
  threshold = request.args.get('threshold')

  # since the api gets run in the main folder, we need to replace the default
  # filepath to be one level lower for config_file_path
  if threshold is None:
    input_type = detect_format(
      "all",
      data,
      config_file_path="pycrossva/resources/mapping_configuration_files/"
    )
  else:
    input_type = detect_format(
      "all",
      data,
      config_file_path="pycrossva/resources/mapping_configuration_files/",
      threshold=float(threshold)
    )

  if input_type is None:
    input_type = "Error: No Match"

  return input_type
