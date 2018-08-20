Copy the gmailtwigman folder in your site-packages (or dist-packages) of python2.X to make the module available in your python script.
(Update: Yesterday I figured out, that you can keep it alternatively in your script folder and access to it equally. <br />
|- myscript.py <br />
|- gmailtwigman )

For e.g. '/usr/lib/python2.7/dist-packages/gmailtwigman' or 'C:\\Python27\\Lib\\site-packages\\gmailtwigman\\'.

Then follow the septs on: https://developers.google.com/gmail/api/quickstart/python

!!!!IMPORTANT!!!!! If you want to send mails or allow other operations, look at https://developers.google.com/gmail/api/auth/scopes
and edit the 'SCOPE' variable. In this example I used https://mail.google.com/ as you can see in the 'gettoken.py'.

Follow the quickstart, and create your 'credentials.json' and 'token.json'. Or if you already have your 'credentials.json',
copy it in this folder, edit the libPath-variable and run the 'gettoken.py' (it should be the same like the quickstart.py from Google).

Finally you should be able to import the gmailtwigman module in your script and send an email -> mailexample.py


Note:
-----
The reason why I uploaded the project is, that I struggled a few hours to send an simple email over gmail. I tried it with the smtplib at first
and it worked instant for other SMTP servers like gmx. But with the Google script I ran into a lot of strange errors (sure it's why I'm not python pro).
For example: If I tried to put the code from the sender.py into the gmail.py it stopped working. Out of nowhere python had problems with the print function,
even if I still used python2. Normally I'm using python3, so maybe it's because of wrong spaces and tabs in my function?

An other error I recieved was: "An error occurred: <HttpError 403 when requesting https://www.googleapis.com/gmail/v1/users/<mailaddress>/messages/send?alt=json returned "Delegation denied for <mailadress>">". <br />
The solution was to not use my email address as userId. Instead I used again 'me' and it worked!



