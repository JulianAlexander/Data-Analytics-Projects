# Belly Button Biodiversity Web App:

Using Python, SQLAlchemy, JavaScript, and Flask, I've built an interactive web app which explores the Belly Button Biodiversity Dataset: http://robdunnlab.com/projects/belly-button-biodiversity/

## Step 1: Flask API
Using Flask, I've designed an API for the Belly Button dataset and to serve the HTML and JavaScript required for the dashboard page. The Flask app references a sqlite database file created using Python and SQLAlchemy, and also reads the CSV data directly into a Pandas DataFrame. The data is output as JSON in each of the routes in the flask_app file.

The dashboard landing page uses a template created with bootstrap in index.html. 

Below are the Flask API routes:
```@app.route("/")
    """Return the dashboard homepage."""
@app.route('/names')
    """List of sample names.

    Returns a list of sample names in the format
    [
        "BB_940",
        "BB_941",
        "BB_943",
        "BB_944",
        "BB_945",
        "BB_946",
        "BB_947",
        ...
    ]

    """
@app.route('/otu')
    """List of OTU descriptions.

    Returns a list of OTU descriptions in the following format

    [
        "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
        "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
        "Bacteria",
        "Bacteria",
        "Bacteria",
        ...
    ]
    """
@app.route('/metadata/<sample>')
    """MetaData for a given sample.

    Args: Sample in the format: `BB_940`

    Returns a json dictionary of sample metadata in the format

    {
        AGE: 24,
        BBTYPE: "I",
        ETHNICITY: "Caucasian",
        GENDER: "F",
        LOCATION: "Beaufort/NC",
        SAMPLEID: 940
    }
    """
@app.route('/wfreq/<sample>')
    """Weekly Washing Frequency as a number.

    Args: Sample in the format: `BB_940`

    Returns an integer value for the weekly washing frequency `WFREQ`
    """
@app.route('/samples/<sample>')
    """OTU IDs and Sample Values for a given sample
    [
        {
            otu_ids: [
                1166,
                2858,
                481,
                ...
            ],
            sample_values: [
                163,
                126,
                113,
                ...
            ]
        }
    ]
    """
```

# Step 2: Use Plotly.js to build webpage

Using Plotly, we create the interactive charts that will populate the home page dashboard.
I created a function, optionChanged(), which fetches all of the sample names and adds them to a dropdown list (this is achieved using Plotly.d3.json). Every time a sample is chosen, the data is fetched from the Flask API.
A pie chart and bubble chart are created using the data from /sample/<sample> and /otu.





