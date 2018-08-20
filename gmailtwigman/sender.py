# Main parts from https://github.com/gsuitedevs/python-samples/blob/master/gmail/quickstart/quickstart.py
#
# Edit by:	https://github.com/Twigman
# Date: 	19.08.2018

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import gmail


SCOPES = 'https://mail.google.com/'

# absulute path
# change it to your lokation
libPath = '/usr/lib/python2.7/dist-packages/gmail-twigman/'

def SendEmail(fromEmail, toEmail, subject, body):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    store = file.Storage(libPath + 'token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(libPath + 'credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

	# DO NOT ENTER YOUR EMAIL HERE!
	# Keep it like it is!
    userId = 'me'
	
    gmailMsg = gmail.CreateMessage(fromEmail, toEmail, subject, body)
    return gmail.SendMessage(service, userId, gmailMsg)
	
