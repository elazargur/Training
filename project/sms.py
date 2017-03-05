from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "AC944ad52f2eafea8cbdda2dccfb398758"
AUTH_TOKEN = "911a853242ad467fab689c6b2beae875"
MY_NUM = "+16465937531"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+972524642459",
    from_= MY_NUM,
    body="Love!",
)
