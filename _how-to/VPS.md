# Virtual Private Server (VPS) at Digitalocean 
The app has to live somewhere. A cheap way is to rent your own VPS server, on which you can then also run many other things.

### Sign up

* Click my [referral-link to receive **your 10$ bonus**](https://m.do.co/c/f934b16d6302) when signing up. (Please [retweet](https://twitter.com/drandreaskruger/status/687910849059635200), thanks).
* Sign up, using your credit card (will only be credited when above those 10$, i.e. 2 months of the smallest droplet).
* Confirm email.

### Security: SSH key
This is optional! You can also simply password-protect the SSH access to your droplet. I like SSH keys because I don't have to type my password each time: 

* open the [Setting ... User ... Security ...](https://cloud.digitalocean.com/settings/security) page.
* read: '[How To Use SSH keys With Droplets](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-putty-on-digitalocean-droplets-windows-users)'
* PuTTYgen ... 
  * 4096 ... Generate ... move mouse
  * Save public Key ... Save private key
  * 'Public key for pasting into OpenSSH' ...:   
  Copy, paste into [digitalocean 'Add SSH key' form](https://cloud.digitalocean.com/settings/security), press green "Create" button

### New droplet
Now we are creating the smallest possible "droplet", with 512 MB RAM, and Debian Linux. 

**Costs:** As long as it exists (i.e. it has an IP address assigned), it costs 0.16 $ per day, even if is switched off. If you want to pause paying, open the [admin interface of the droplet](https://cloud.digitalocean.com/droplets): Power it off, take a snapshot, then destroy the droplet. Later, you can continue, using that now ready configured snapshot as the image for a new droplet. Very easy. But for now, let's start: 

[Create new droplet](https://cloud.digitalocean.com/droplets/new)
* Image: Debian 8.2 x64,   
Size: $5/month (512MB, 20GB, 1000GB),  
Region: New York (close to Europe AND California),  
(optional:) Add your SSH keys
* Wait 55 seconds
* copy the IP address, e.g. **208.68.38.174** (*in my case*; of course, you use yours ... )
  
### SSH access
* You need an SSH client, e.g. [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).
* IP: 208.68.38.174, port: 22, Type: SSH
* (optional, if SSH key from above):
  * Connection ... Data ... Auto-login username: root
  * Connection ... SSH ... Auth ... Private key file for authentication:  the *.ppk file that you saved (above)
* (optional): I change the background color for each droplet, to be able to distinguish them
* Session ... Save Session Name ... Save 
* Open
 
### Dependencies
Update, and install dependencies, and useful tools
This prepares the system

    apt-get update && apt-get -y upgrade
    apt-get install -y sudo nano lynx tree screen python-pip git
    sudo pip install -U pip
    sudo pip install Django iptools requests jsonfield coinbase
    
    sudo pip --version; python --version; python -c "import django; print('django '+django.get_version())"
    
I got: pip 7.1.2, Python 2.7.9, django 1.9.1

### Run app

Superb. Your server is prepared. Please see [configure.md](configure.md) now, how to get the app running.

### Future work needed

This is a proof of concept project only. If you want to use this in production, I suggest you consider:

* running the django app with [uWSGI](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-14-04) behind an [nginx webserver](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-debian-8).
* closing the access with a firewall with e.g. [iptables](https://www.digitalocean.com/community/tutorials/how-the-iptables-firewall-works).
* coding more, and better [reactions](../buyme/reaction.py) to when your client has paid you, see [TODO.md](TODO.md).
  
