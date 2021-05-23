# Bioinformatics App in Dash

A bioinformatics project using _Dash_ & _BioPython_ with _Plotly_ visulizations.

The start point for the application is in the index.py file.

There are four main components to this application:

- Sequence Viewer (sequenceViewer.py)
- Alignment Viewer (alignment.py)
- Table View (DataTable.py)
- Interaction Viewer (interactivity.py)

The code for these can be found in the "apps" folder.

The database included in this repo was built using the BioSQL schema, with an extra table for peptides being added.

A new database file can be created by running the init_db.py file. This will create an empty database. To populate this,
the sql statements within sqlstatements.txt must be run.

A blastdb folder has been included within this repo, although it is not currently used in the project. The blastdb was created
to allow Local BLAST functionality to be added in future development.

Dependabot has been set up with this repo through the file within the .github folder.

## Development

```shell script
git clone https://github.com/james0209/dash-bioinformatics.git
```

### Install

```shell script
git clone https://github.com/james0209/dash-bioinformatics.git

# using pip/python
python -m venv env
    # linux/mac
    source env/bin/activate
    # windows
    .\env\Scripts\activate
cd dash-bioinformatics
pip install -r requirements.txt
```

### Run

```shell script
python index.py
```

## References

Dash - <https://plotly.com/dash/>

BioPython - <https://biopython.org/>

BioSQL - <https://biosql.org/>

Dash Bootstrap Components - <https://github.com/facultyai/dash-bootstrap-components>

The Sainsbury Laboratory - <http://www.tsl.ac.uk/>
