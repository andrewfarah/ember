from twilio.rest import TwilioRestClient

account_sid = "ACc16b75896fa3e50970c248c2571fadd2" # Your Account SID from www.twilio.com/console
auth_token  = "9e88494a995b3c1d2e3550b92e0bd4f4"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Ember says, Hello World.",
    to="+17038872869",    # Replace with your phone number
    from_="+12403485098") # Replace with your Twilio number

print(message.sid)