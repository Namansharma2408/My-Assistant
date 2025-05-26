from twilio.rest import Client

account_sid = ACCOUNT_SID
auth_token = 'd19ad2b44ae32953e8c0db2584ad32f5'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+918708450013'
)

print(message.sid)