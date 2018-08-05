from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1aT6RikRvebB_Hh98l9LRbF2J7OrSLkyG3X71JqIqvaY'
SAMPLE_RANGE_JOHAN = 'Johan!A2:B'
SAMPLE_RANGE_ANDREAS = 'Andreas!A2:B'



def main():
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
    print(SAMPLE_RANGE_JOHAN.split("!")[0])
    result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range=SAMPLE_RANGE_JOHAN).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('Datum, Minuter:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(u'%s, %s' % (row[0], row[1]))

   # Call the Sheets API
    print(SAMPLE_RANGE_ANDREAS.split("!")[0])
    result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range=SAMPLE_RANGE_ANDREAS).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('Datum, Minuter:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(u'%s, %s' % (row[0], row[1]))


if __name__ == '__main__':
    main()