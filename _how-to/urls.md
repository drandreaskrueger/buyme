# URLs

### URLs to try on localhost 
e.g. for dev'ing in eclipse:

GET:  
[http://localhost:8000/buyme/](http://localhost:8000/buyme/)

[http://localhost:8000/buyme/hook/0000000139798743472/](http://localhost:8000/buyme/hook/0000000139798743472/)  
[http://localhost:8000/admin](http://localhost:8000/admin)

POST:
  
    curl -X POST -d "name=Andreas%20Krueger&project=buyme" http://localhost:8000/buyme/hook/0000000139798743472/
    curl -X POST -d "name=Andreas%20Krueger&project=buyme" http://localhost:8000/buyme/hook/5555555555555555555/  

BTW: On windows, I got ``curl`` via [chocolatey](https://chocolatey.org/):

    choco install curl 

	
### URLs in the cloud 

http://208.68.38.174:8000/buyme

http://208.68.38.174:8000/admin

http://208.68.38.174:8000/buyme/hook/0000000139798743472/


    curl -X POST -d "name=Andreas%20Krueger&project=buyme" http://208.68.38.174:8000/buyme/hook/0000000139798743472/  
    curl -X POST -d "name=Andreas%20Krueger&project=buyme" http://208.68.38.174:8000/buyme/hook/5555555555555555555/
  
Of course - replace the 208.68.38.174 with *your IP address*.

#### Hint: 
The [last step (= reactions.py)](../_how-to/#flow) will only be executed if the webhook receives data from the correct (coinbase) IP range. For debugging that, just press the "*Start a new payment*" below the "View your receipt. Return to ..." button. Each payment causes coinbase to send a new notification to the webhook. 

