
**this text is unready**


### testnet sandbox

Server is started with 

    python manage.py runserver 0.0.0.0:8000
    
Then the checkout is created:

    ... creating a coinbase checkout.
    Callback: Using notifications_url='http://208.68.38.174:8000/buyme/hook/9999999876543765456/' for callback.
    checkout.warnings=None
    redirecting to coinbase: https://sandbox.coinbase.com/checkouts/ee0f3b6999fa88729b769af0187498b5
    [19/Jan/2016 06:21:38] "POST /buyme/ HTTP/1.1" 302 0
    
then when SANDBOX payment done:

    Received POST request on 'hook/name' : 9999999876543765456
    '54.175.255.207' is a coinbase IP, all cool. trustIP=True. sending email success = 1
    [19/Jan/2016 06:24:05] "POST /buyme/hook/9999999876543765456/ HTTP/1.1" 200 33


So in case of the testnet, the received notification callback request is well-formed. --> (200, OK)



### mainnet

Server is started with 

     python manage.py runserver 0.0.0.0:8001
    
Then the checkout is created:

    ... creating a coinbase checkout.
    Using notifications_url='http://208.68.38.174:8001/buyme/hook/9999999876543765456/' for callback.
    checkout.warnings=None
    redirecting to coinbase: https://coinbase.com/checkouts/21d38415a95aaebb704c02e9512fdd54
    [19/Jan/2016 05:50:45] "POST /buyme/ HTTP/1.1" 302 0

then when MAINNET payment done ...

    [19/Jan/2016 05:56:59] "POST /buyme/hook/9999999876543765456/ HTTP/1.1" 400 26

So (400, BAD REQUEST) ... = something in the mainnet callback POST request is malformed:

> error 400:
> A 400 means that the request was malformed. In other words, the data stream sent by the client to the server didn't follow the rules.
> In the case of a REST API with a JSON payload, 400's are typically, and correctly I would say, used to indicate that the JSON is invalid in some way according to the API specification for the service.
> http://stackoverflow.com/a/19671511


### thoughts
The differences between mainnet and testnet in my code are the port numbers 8000 and 8001, and the 3 constants in:
 
    client=Client(API_KEY, API_SECRET, base_api_uri=API_BACKEND_URL)

but the problem appears not when creating the checkout but when receiving the callback.

The other difference is ``djangosite.settings.DEBUG=False`` --> that is causing the problem! 


