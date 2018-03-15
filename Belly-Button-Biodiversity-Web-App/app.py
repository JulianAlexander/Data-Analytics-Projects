# import necessary libraries
from flask import Flask, jsonify, g, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import json

dialect = 'sqlite'
port = 3306
database = 'bellybutton.sqlite'

engine = create_engine(f'{dialect}:///{database}')
# reflect an existing database into a new model
# @TODO: YOUR CODE HERE
Base = automap_base()
Base.prepare(engine, reflect=True)

print(Base.classes.keys())
# reflect the tables
# @TODO: YOUR CODE HERE

# Save references to the invoices and invoice_items tables
# @TODO: YOUR CODE HERE

# Create our session (link) from Python to the DB
# @TODO: YOUR CODE HERE
session = Session(bind=engine)

#Station = Base.classes.station

sampleNames = Base.classes.sampleNames
OTU = Base.classes.OTU
metadata = Base.classes.metadata
washingFreq = Base.classes.washingFreq
sampleValues = Base.classes.sampleValues 

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bellybutton.sqlite"

db = SQLAlchemy(app)

def getNames():
    names = session.query(sampleNames).all()
    names_lst = []
    for row in names:
        names_lst.append(row.sNames)
    names_json = jsonify(names_lst)
    return names_json

def getOTU():
    otu_descrip = session.query(OTU).all()
    otu_lst = []
    for row in otu_descrip:
        otu_lst.append(row.OTU_descriptions)
    return jsonify(otu_lst)

def getMetadata():
    metadata_q = session.query(metadata)
    meta_lst = []
    for row in metadata_q:
        metadatadict = {}
        metadatadict['AGE'] = row.AGE
        metadatadict['BBTYPE'] = row.BBTYPE
        metadatadict['ETHNICITY'] = row.ETHNICITY
        metadatadict['GENDER'] = row.GENDER
        metadatadict['LOCATION'] = row.LOCATION
        metadatadict['SAMPLEID'] = row.SAMPLEID
        meta_lst.append(metadatadict)
    return jsonify(meta_lst)

def getMetaSample(sample):
    metadata_q = session.query(metadata).filter(metadata.SAMPLEID == sample[3:])
    meta_lst = []
    for row in metadata_q:
        metadatadict = {}
        metadatadict['AGE'] = row.AGE
        metadatadict['BBTYPE'] = row.BBTYPE
        metadatadict['ETHNICITY'] = row.ETHNICITY
        metadatadict['GENDER'] = row.GENDER
        metadatadict['LOCATION'] = row.LOCATION
        metadatadict['SAMPLEID'] = row.SAMPLEID
        meta_lst.append(metadatadict)
    return jsonify(meta_lst)

def getSampleValues(sample):
    sample_ID = sample[3:]
    sample_df = pd.read_sql('batchTable', con = engine)
    sample_values = sample_df.sort_values([sample_ID], ascending = False)
    sampleDict = dict(sample_values)

    sample_lst = []
    sample_dict = {}
    sample_dict['otu_ids'] = sample_values['OTU ID #'].tolist()
    sample_dict['sample_values'] = sample_values[sample_ID].tolist()
    sample_lst.append(sample_dict)
    return jsonify(sample_lst)

def getWashFreq(sample):
    washFreq = session.query(washingFreq).filter(washingFreq.sNames == sample).all()
    for row in washFreq:
        return jsonify(row.washFreq)

#################################################
# Routes
#################################################


@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/names")
def names():
    return getNames()
        
@app.route("/otu")
def otu():
    return getOTU()

@app.route("/metadata")
def retmetadata():
    return getMetadata()

@app.route("/metadata/<sample>")
def retSampleMetadata(sample):
    return getMetaSample(sample)

@app.route("/samples/<sample>")
def returnSamples(sample):
    return getSampleValues(sample)

@app.route("/wfreq/<sample>")
def wfreq(sample):
    return getWashFreq(sample)

if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    # YOUR CODE GOES HERE
    app.run(debug=True)
    raise NotImplementedError()
