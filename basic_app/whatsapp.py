

from twilio.rest import Client 
 
account_sid = 'ACf98530c3e0be963ce90d7148408fdf6d'
auth_token = 'e5e4b70336df2b137fba3b1a6bb8e80f'
client = Client(account_sid, auth_token) 


def send_message(mesg):
    message = client.messages.create(
        body=mesg,
        from_='whatsapp:+14155238886',
        to='whatsapp:+918355852271'
    )
    print(message.sid)


