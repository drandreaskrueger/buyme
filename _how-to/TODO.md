# TODO

## TODO coinbase

### Default webhook not working

When the API key is created, the default *notifications* set there, sent to my app hook: ``http://208.68.38.174:8000/buyme/hook/9999999911111263534/`` ...  
... just doesn't work. It never gets called.

I solve it by setting individual notifications when creating the callback.
  
Perhaps this influences the default callback, so that the above default notification stops working? Dunno.

### 
When a [checkout is created](https://developers.coinbase.com/api/v2#create-checkout) the money always ends up in the primary account:

> All checkouts and subsequent orders created using this endpoint are created for merchant’s primary account.

I would actually like to keep incoming money in a dedicated account. Please consider to open your concept to that. Thanks.
 

  
## TODO me

### Security
The file ```` is not the ideal place for the API_SECRET, and the EMAIL_USER_PASSWORD.

One problem is that it might accidentially get uploaded to git. I have already put it in .gitignore, but even then, it happened, somehow.  
When you have input your own credentials, you can remove it from the index:
 
    git rm buyme/configPrivate.py --cached
    
But that is not the final say in security. Where to best store sensitive data?

