# TODO

## TODO coinbase

### Default webhook not working (bug?)

When the API key is created, the default *notifications* set there, sent to my app hook: ``http://208.68.38.174:8000/buyme/hook/0000000139798743472/`` ...  
... just doesn't work. It never gets called.

I solve it by setting individual notifications when creating the callback.
  
Perhaps this influences the default callback, so that the above default notification stops working? Dunno.

### checkout money into dedicated account (feature request)
When a [checkout is created](https://developers.coinbase.com/api/v2#create-checkout) the money always ends up in the *primary account*:

> All checkouts and subsequent orders created using this endpoint are created for merchant's primary account.

I'd like it better to keep incoming money in one *dedicated account* **per app**. Please consider to open your concept to that. Thanks.
 

  
## TODO me

### Security
The file [configPrivate.py](../buyme/configPrivate.py) is not the ideal place for the API_SECRET, and the EMAIL_USER_PASSWORD.

One problem is that it might accidentially get uploaded to git. I have already put it in .gitignore, but even then, it happened, somehow.  When you have input your own credentials, you can remove it from the git index:
 
    git rm buyme/configPrivate.py --cached
    git update-index --assume-unchanged buyme/configPrivate.py
    
But that is not the final say in security. Where to best store sensitive data?

### Mispayments
I tried to send to a checkout address many hours later. It worked! And it created a callback on my webhook!   

But as The *wrong amount of money is sent to an address*, it is counted as 'mispayment', see [output/notification_mispayment.email.txt](output/notification_mispayment.email.txt) versus [output/notification_correctPayment.email.txt](output/notification_correctPayment.email.txt). 

Recognize that, and treat differently.

EDIT: Mostly done. The ``notification.data.resource.status`` is saved into the 'paid' object (= 'expired' or 'paid'). So immediately visible.

### Finishing touch
favicon.ico


