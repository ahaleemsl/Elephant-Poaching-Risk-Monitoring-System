# import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

# this is the URL to an image file we're going to send in the MMS
media = "https://Your_Media_image's_Link"

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send MMS to any phone number that MMS is available
client.api.account.messages.create(to="Your_Phone_Number",
                                   from_="Your_Twilio_Number",
                                   media_url=media
                                   body="Human Presence detected",
                                   "Location:"
                                   "Latitude:"= media(maps.lat()).found()"
                                   "Longitude:"=media(maps.long()).found()"
                                   media_url=media)