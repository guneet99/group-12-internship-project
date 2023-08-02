from twilio.rest import Client
def smsSender(message):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message,
                        from_='',
                        to=''
                    )

    print(message.sid)


def alertCall():
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            to='',
                            from_='',
                            url=""
                        )

    print(call.sid)