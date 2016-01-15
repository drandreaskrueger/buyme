# Install and configure app

### Coinbase sandbox
I strongly advise, you try this first in the **coinbase sandbox**, in which you can play with money, without spending real money.

* sign up for a 'coinbase sandbox account' at https://sandbox.coinbase.com/signup

Once you got it all running and have fully understood it, you can switch to ``PRODUCTION=True`` in [config.py](../buyme/config.py), and instead of the sandbox ... connect it to a real coinbase account at https://www.coinbase.com/signup - and start earning real money.
 
### API key for coinbase access

To be able to create a 'checkout' via API:
* fill in your '[merchant profile](https://sandbox.coinbase.com/merchant_profiles)' until you get a green ``'Your merchant profile has been updated.'``

Then 
* at https://sandbox.coinbase.com/settings/api --> *Create New API key*
  * with *permission*: ``wallet:checkouts:create``
  * with *notifications* sent to the app hook: ``http://208.68.38.174:8000/buyme/hook/9999999911111263534/``  
    (In my case. Change 208.68.38.174 to your IP.)
  * Create. Then 'show' the 'API Key details' 

* --> ``API_KEY`` & ``API_SECRET`` into [configPrivate.py](../buyme/configPrivate.py) (that file is in .gitignore, so that it is not committed to git).

## django app
Prepare the server, install dependencies, etc - see '[VPS ... dependencies](VPS.md#dependencies)'.

clone this from github

    git clone https://github.com/drandreaskrueger/buyme.git
    cd buyme

### django database
The db.sqlite3 database has to be initialized *once*:

	python manage.py makemigrations buyme
    python manage.py migrate
    python manage.py createsuperuser

And the static files made available:

    python manage.py collectstatic

### Run Server
    python manage.py runserver 0.0.0.0:8000

### Testing
Now you can try all the [URLs in the cloud](create-project-and-app.md). In my case the base url is:

--> http://208.68.38.174:8000/buyme/
