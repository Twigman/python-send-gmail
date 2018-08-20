Copy the gmail folder in your site-packages (or dist-packages) of python2.X to make the module available in your python script.

For e.g. '/usr/lib/python2.7/dist-packages/gmailtwigman' or 'C:\\Python27\\Lib\\site-packages\\gmailtwigman\\'.

Then follow the septs on: https://developers.google.com/gmail/api/quickstart/python

!!!!IMPORTANT!!!!! If you want to send mails or allow other operations, look at https://developers.google.com/gmail/api/auth/scopes
and edit the 'SCOPE' variable. In this example I used https://mail.google.com/ as you can see in the 'gettoken.py'.

Follow the quickstart, and create your 'credentials.json' and 'token.json'. Or if you already have your 'credentials.json',
copy it in this folder, edit the libPath-variable and run the 'gettoken.py' (it should be the same like the quickstart.py from Google).

Finally you should be able to import the gmailtwigman module in your script and send an email -> mailexample.py

