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
#### Security API_SECRET
The file [configPrivate.py](../buyme/configPrivate.py) is not the ideal place for the API_SECRET, and the EMAIL_USER_PASSWORD.

One problem is that it might accidentially get uploaded to git. I have already put it in .gitignore, but even then, it happened, somehow.  When you have input your own credentials, you can remove it from the git index:
 
    git rm buyme/configPrivate.py --cached
    git update-index --assume-unchanged buyme/configPrivate.py
    
But that is not the final say in security. Where to best store sensitive data?

#### Security Hooknames
Instead of the hardcoded placeholders (HOOKS in config.py), of course a final production version needs individually generated hooknames. Probably simply stored as one more field in the 'newBuy' structure. When webhook data is received, the hookname is compared to all those existing hooknames.  

#### Security HTTPS
The finaly production version should run as an uWSGI app behind an nginx server (see [VPS.md](VPS.md)), with https enabled. 

### Mispayments
I tried to send to a checkout address many hours later. It worked! And it did create a callback on my webhook!   

But it is counted as 'mispayment' (probably similar to if the *wrong amount of money is sent to a given address*). Examples - see [notification_mispayment.email.txt](../output/notification_mispayment.email.txt) versus [notification_correctPayment.email.txt](../output/notification_correctPayment.email.txt). 

EDIT: Mostly done: Code recognizes that, and treats it differently. The ``notification.data.resource.status`` is saved into the 'paid' object (= 'expired' or 'paid'), and put into the email. So it is immediately visible.

### Reactions
When a payment is received a lot of additional actions can be triggered. See [reactions.py](../buyme/reactions.py#L107-L132).

### Finishing touch
favicon.ico

