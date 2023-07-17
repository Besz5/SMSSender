from twilio.rest import Client

account_sid = 'AC2d54c6f6d8c6331968bac2df10bfbc8c'
auth_token = 'SAHD7511KJD23sajcn123kdc'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12266024690',
    body='HelloBello',
    to='+16472617454'
)

print(message.sid)