# Andreas dunderkod, johan är noob
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools

from flask import render_template
from flask import Flask
app = Flask("Server")

@app.route("/")
def hello():
	return render_template('hemsida.html')

@app.route("/traininghours")
def traininghours():
	return render_template('traininghours.html', database=fetchdata())

@app.route("/testresults")
def testresults():
	return render_template('testresults.html')





# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1aT6RikRvebB_Hh98l9LRbF2J7OrSLkyG3X71JqIqvaY'
SAMPLE_RANGE_JOHAN = 'Johan!A2:B'
SAMPLE_RANGE_ANDREAS = 'Andreas!A2:B'


def fetchdata():
    """Shows basic usage of the Sheets API.

    Prints values from a sample spreadsheet.
    """
    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sum_minutes_johan = 0
    result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range=SAMPLE_RANGE_JOHAN).execute()
    values_johan = result.get('values', [])
    for rows in values_johan:
    	sum_minutes_johan = int(rows[1])+sum_minutes_johan
    print(sum_minutes_johan)


   # Call the Sheets API
    sum_minutes_andreas = 0
    result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range=SAMPLE_RANGE_ANDREAS).execute()
    values_andreas = result.get('values', [])
    for rows in values_andreas:
    	sum_minutes_andreas = int(rows[1])+sum_minutes_andreas
    print(sum_minutes_andreas)

    return [sum_minutes_johan, sum_minutes_andreas]




if __name__ == '__main__':
	app.run(debug=True)


