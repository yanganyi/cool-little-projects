import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def load_csv_data(csv_file_path):
    """Loads CSV data from a file and returns it as a list of dictionaries."""
    data = []
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_file_path}'")
        return None
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data", methods=['GET','POST'])
def data_page():
    csv_file = "data.csv"
    csv_data = load_csv_data(csv_file)
    headers = csv_data[0].keys() if csv_data else []

    if request.method == "GET":
        return render_template(
            'data.html',
            csv_data=csv_data,
            headers=headers,
            selected_column="",
            filter_value=""    
        )

    if request.method == "POST":
        filter_column = request.form.get('filter_column')
        filter_value = request.form.get('filter_value')

        filtered_data = csv_data

        if filter_column and filter_value:
            filtered_data = [
                row for row in csv_data
                if filter_column in row and filter_value.lower() in str(row[filter_column]).lower()
            ]

        return render_template(
            'data.html',
            csv_data=filtered_data,
            headers=headers,
            selected_column=filter_column,
            filter_value=filter_value
        )

if __name__ == "__main__":
    app.run()