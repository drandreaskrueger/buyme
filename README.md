# buyme v0.16
*Coinbase payments made easy.* Django app to buy time with BTC payments. The whole process.
  
= Learning how to include **Coinbase checkouts**, incl. properly reacting to webhook callback data. 

## Try it live:

(1) FRONTEND: **http://208.68.38.174:8000/buyme** to create the product & checkout.

(2) Get a free [coinbase sandbox](https://sandbox.coinbase.com/) account to pay with testnet3 coins. 

(3) BACKEND: http://208.68.38.174:8000/admin (**user:** tester, **password:** tipmeplease)

*Or* see [output/](output/) for some screenshots & logfiles.

## Quickstart

Prepare [server](_how-to/VPS.md):

    apt-get update && apt-get -y upgrade
    apt-get install -y sudo nano lynx tree screen dos2unix wget curl python-pip git 
    sudo pip install -U pip
    sudo pip install Django iptools requests jsonfield coinbase

Clone and configure this repo:

    git clone https://github.com/drandreaskrueger/buyme.git
    cd buyme
    nano buyme/configPrivate.py

Fill in your API_KEY and API_SECRET, see [configure.md#api-key-for-coinbase-access] (https://github.com/drandreaskrueger/buyme/blob/master/_how-to/configure.md#api-key-for-coinbase-access). Forget email, for now. 

Initialize Django & DB: 

    python manage.py makemigrations buyme
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py collectstatic
    
Run server: 

	python manage.py runserver 0.0.0.0:8000
	
Open in browser (change to your IP address):

* http://208.68.38.174:8000/buyme = the app
* http://208.68.38.174:8000/admin = admin pages for the DB (**user:** tester, **password:** tipmeplease)
    
## More information:
[![diagrams and more](_how-to/img/thumbs.png)](_how-to/README.md)

See [_how-to/README.md](_how-to/README.md) for diagrams, and manuals.

## You might want to edit:
* in [buyme/](buyme/) = django *app*:
  * [configPrivate.py](buyme/configPrivate.py) = coinbase KEY (*), and email (optional). 
  * [config.py](buyme/config.py) = constants that influence some app properties.
  * [templates/](buyme/templates/) = html template of buyme/-page with form
* [djangosite/settings.py](djangosite/settings.py) = django project which loads the app

(*) = MUST EDIT. Keep everything else unchanged, for a starter.

## BUG
There is a [bug in the coinbase notification system](https://github.com/drandreaskrueger/coinbaseTestbed/blob/master/bugs/HOST-header_empty.md) which prevents Django from accepting notification POST requests from coinbase, as they do not comply with RFC 1034/1035. I have already reported that bug in several places, e.g. [here](https://hackerone.com/reports/113936). 

Until that is fixed, you must not switch djangosite-->settings.py ``DEBUG = False`` ([line 30](https://github.com/drandreaskrueger/buyme/blob/master/djangosite/settings.py#L30), and in my edits in [line 117](https://github.com/drandreaskrueger/buyme/blob/master/djangosite/settings.py#L117)).  

With ``DEBUG=True`` Django is more sloppy with faulty requests, seemingly. But the [official Django code](https://github.com/django/django/blob/master/django/conf/project_template/project_name/settings.py-tpl#L25-L26) **strongly warns against that**:

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    
So ... the current Coinbase system forces you to violate essential Django security. 

**TL;DR:** Do not run in production - until Coinbase has fixed this. 


## Time estimates
Using my new tool [FiledatePunchcard](https://github.com/drandreaskrueger/FiledatePunchcard) to give a rough estimate of the time that I have invested into this. 

    Each 'x' represents a 30 minute block:
    (Filled up blocks of size 6, i.e. approx 180 minutes.)
    
    2016-01-13|----------------------------------------x       |
    2016-01-14|                        x         x             |
    2016-01-15|                         xxxxxxxxxxxxxxxxxxxxx  |
    2016-01-16|                                                |
    2016-01-17|                             xxxxxxxxxxxxxxxxx  |
    2016-01-18|               xxxxxxxxxxxxxxxxxxxxxxxxx        |
    2016-01-19|            xxxxxxxxxxxxxxxxxx                  |
    2016-01-20|                         xxx               x    |
    2016-01-21|                                                |
    2016-01-22|                                                |
    2016-01-23|                                                |
    2016-01-24|                                                |
    2016-01-25|                                                |
    2016-01-26|                                    xxxxxxx     |
    2016-01-27|                                                |
    2016-01-28|                                                |
    2016-01-29|                                                |
    2016-01-30|                                                |
    2016-01-31|                                                |
    2016-02-01|                                           x----|
    
    With 30-minute blocks, the number of hours is approx 48.0

Probably more, because the above is only registering filedates, which are overwritten with each (non-committed) file saving. 


## donation ware!
(C) 2016 Andreas Krueger  
**If you like this, show it:** [BTC] [1JjSXcUKEmZGTvdC9BGbM6RrkGVdApape5](http://blockr.io/address/info/1JjSXcUKEmZGTvdC9BGbM6RrkGVdApape5)   
No Coinbase account yet? Please [use my referral](https://www.coinbase.com/join/andreaskrueger), to give me and you 10$ bonus.

## Hire me
hire (at) andreaskrueger (dot) de
  
