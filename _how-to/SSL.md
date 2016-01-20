# SSL = HTTP**S**

Haven't tried it out yet, but done some research:

### stunnel
* stunnel tutorial at [isotoma](https://www.isotoma.com/blog/2012/07/17/running-a-django-dev-instance-over-https/)
* at [ianlewis](https://www.ianlewis.org/en/testing-https-djangos-development-server)

### RunServerPlus

    pip install django-extensions pyOpenSSL
    python manage.py runserver_plus --cert cert
    
* [Googol](http://stackoverflow.com/questions/7610394/how-to-setup-ssl-on-a-local-django-server-to-test-a-facebook-app/18694704#18694704) tutorial
* [readthedocs](https://django-extensions.readthedocs.org/en/latest/runserver_plus.html#ssl) manual of django-extensions

### django-sslserver

    pip install django-sslserver
    INSTALLED_APPS = (... "sslserver",
    python manage.py runsslserver [--addrport 127.0.0.1:9000]
    
* [sourcecode](https://github.com/teddziuba/django-sslserver)
* found it through [jdero](http://stackoverflow.com/questions/7610394/how-to-setup-ssl-on-a-local-django-server-to-test-a-facebook-app/18167433#18167433)


## buy SSL certificate
* how to [install](https://www.digitalocean.com/community/tutorials/how-to-install-an-ssl-certificate-from-a-commercial-certificate-authority) digitalocean tutorial
* [9$ per year](https://www.namecheap.com/security/ssl-certificates/domain-validation.aspx)
* [30$ per year](https://www.hosteurope.de/en/SSL-Zertifikate/)
* [20 sellers list](http://webdesign.about.com/od/ssl/tp/cheapest-ssl-certificates.htm)