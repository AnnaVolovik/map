"""This module helps storing and updating geo locations."""

import csv
import os

from flask import Flask, request
from flask_cors import CORS


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

filename = os.path.join(app.root_path, '..', 'public', 'markers.csv')


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/", methods=['GET'])
def get_markers():
    """Получить список маркеров из бд."""
    markers = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            markers = [row for row in reader]
    except FileNotFoundError:
        pass
    return {'data': markers}


@app.route("/update", methods=["POST"])
def update_markers():
    """Обновить список маркеров в таблице."""
    data = request.get_json()

    i = 0
    markers = []
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'lat', 'lng']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for el in data:
            el["id"] = i
            writer.writerow(
                {
                    "id": el["id"],
                    "lat": el["lat"],
                    "lng": el["lng"],
                })
            markers.append(el)
            i += 1

    return {'data': markers}


if __name__ == "__main__":
    app.run()
