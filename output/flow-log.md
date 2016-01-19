# Log of the whole flow

Starting Django server

    python manage.py runserver 0.0.0.0:8000
    
    Performing system checks...
    System check identified no issues (0 silenced).
    January 19, 2016 - 13:17:00
    Django version 1.9.1, using settings 'djangosite.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.

## verbose

with ``DEBUG_MESSAGES=True`` verbose step-by-step log printing:  
    
Into browser: http://208.68.38.174:8000/buyme

    showing webpage with form to input credentials
    [19/Jan/2016 13:17:08] "GET /buyme/ HTTP/1.1" 200 3842
    [19/Jan/2016 13:17:08] "GET /static/buyme/clean3d-blue-015-icon.png HTTP/1.1" 304 0
    
Filled in form, press submit:

    POST request received.
    Valid. Saved. Taking form entries, and creating a coinbase checkout.
    Callback: Using notifications_url='http://208.68.38.174:8000/buyme/hook/4dspfcg02p/' for callback.
    client.create_checkout.warnings=None
    redirecting to coinbase: https://sandbox.coinbase.com/checkouts/74a92bafddcb9da7135fd02842ebef5d
    [19/Jan/2016 13:17:19] "POST /buyme/ HTTP/1.1" 302 0
    
When having paid money:

    Received POST request on /hook/4dspfcg02p/
    Hookname recognized.
    trustHook=True
    '54.175.255.205' is a coinbase IP, all cool.
    trustIP=True
    Request is trusted. Calling reactions:
    Paid data saved into DB.
    Sending email success = 1
    [19/Jan/2016 13:17:46] "POST /buyme/hook/4dspfcg02p/ HTTP/1.1" 200 33
    
After payment blue 'back to ...' button:

    [19/Jan/2016 13:17:59] "GET /buyme/thankyou/?order%5Bbutton%5D%5Bdescription%5D=Let+us+SKYPE%3A+I+can+CODE+for+you%2C+RESEARCH+your+topics%2C+ANALYZE+your+DATA%2C+etc.&order%5Bbutton%5D%5Bid%5D=74a92bafddcb9da7135fd02842ebef5d&order%5Bbutton%5D%5Bname%5D=Buy+Time+with+a+Specialist+in+Cryptocurrencies.&order%5Bbutton%5D%5Brepeat%5D=&order%5Bbutton%5D%5Bresource_path%5D=%2Fv2%2Fcheckouts%2F2f95c5a9-1820-5d6f-8b00-ac8ecfa644a5&order%5Bbutton%5D%5Bsubscription%5D=false&order%5Bbutton%5D%5Btype%5D=buy_now&order%5Bbutton%5D%5Buuid%5D=2f95c5a9-1820-5d6f-8b00-ac8ecfa644a5&order%5Bcreated_at%5D=2016-01-19+14%3A17%3A20+%2B0100&order%5Bcustom%5D=&order%5Bevent%5D=&order%5Bid%5D=MTEYDAOL&order%5Bmetadata%5D%5Bduration%5D=15+minutes&order%5Bmetadata%5D%5Bid%5D=3&order%5Bmetadata%5D%5Bprice%5D=19+USD&order%5Breceive_address%5D=n2G1jrUNqPVg7WPQvRcpKmNa4CmcdYzytK&order%5Brefund_address%5D=mz1wkav8VYf1yaffZobY9Zivz141jofDRE&order%5Bresource_path%5D=%2Fv2%2Forders%2F197ed153-be55-5a46-969d-90280f9df69d&order%5Bstatus%5D=completed&order%5Btotal_btc%5D%5Bcents%5D=600000.0&order%5Btotal_btc%5D%5Bcurrency_iso%5D=BTC&order%5Btotal_native%5D%5Bcents%5D=6000.0&order%5Btotal_native%5D%5Bcurrency_iso%5D=USD&order%5Btotal_payout%5D%5Bcents%5D=0.0&order%5Btotal_payout%5D%5Bcurrency_iso%5D=USD&order%5Btransaction%5D%5Bconfirmations%5D=0&order%5Btransaction%5D%5Bhash%5D=&order%5Btransaction%5D%5Bid%5D=569e3778d59e1c74c40001ef&order%5Buuid%5D=197ed153-be55-5a46-969d-90280f9df69d HTTP/1.1" 200 2197

## short
with ``DEBUG_MESSAGES=False``:

    [19/Jan/2016 13:25:26] "GET /buyme/ HTTP/1.1" 200 3842
    [19/Jan/2016 13:25:26] "GET /static/buyme/clean3d-blue-015-icon.png HTTP/1.1" 304 0
    
    [19/Jan/2016 13:25:34] "POST /buyme/ HTTP/1.1" 302 0
    
    [19/Jan/2016 13:25:51] "POST /buyme/hook/oadj5r8cg6/ HTTP/1.1" 200 33
    
    [19/Jan/2016 13:25:55] "GET /buyme/thankyou/?order%5Bbutton%5D%5Bdescription%5D=Let+us+SKYPE%3A+I+can+CODE+for+you%2C+RESEARCH+your+topics%2C+ANALYZE+your+DATA%2C+etc.&order%5Bbutton%5D%5Bid%5D=45adf365e138bfa15251f0e3f1dde461&order%5Bbutton%5D%5Bname%5D=Buy+Time+with+a+Specialist+in+Cryptocurrencies.&order%5Bbutton%5D%5Brepeat%5D=&order%5Bbutton%5D%5Bresource_path%5D=%2Fv2%2Fcheckouts%2F12814239-8ed2-563c-a02f-1bfc30c6f38d&order%5Bbutton%5D%5Bsubscription%5D=false&order%5Bbutton%5D%5Btype%5D=buy_now&order%5Bbutton%5D%5Buuid%5D=12814239-8ed2-563c-a02f-1bfc30c6f38d&order%5Bcreated_at%5D=2016-01-19+14%3A25%3A35+%2B0100&order%5Bcustom%5D=&order%5Bevent%5D=&order%5Bid%5D=LYY9J08Y&order%5Bmetadata%5D%5Bduration%5D=4+hours&order%5Bmetadata%5D%5Bid%5D=4&order%5Bmetadata%5D%5Bprice%5D=200+USD&order%5Breceive_address%5D=mq1iRfswnX6FGJCo9L8dFed864d1aP8XEh&order%5Brefund_address%5D=mqeCBSaHz9ogpgtDxPGRXQEGPanozdoUne&order%5Bresource_path%5D=%2Fv2%2Forders%2F5a1d8dc3-e45c-56ad-bf21-b740145466c9&order%5Bstatus%5D=completed&order%5Btotal_btc%5D%5Bcents%5D=600000.0&order%5Btotal_btc%5D%5Bcurrency_iso%5D=BTC&order%5Btotal_native%5D%5Bcents%5D=6000.0&order%5Btotal_native%5D%5Bcurrency_iso%5D=USD&order%5Btotal_payout%5D%5Bcents%5D=0.0&order%5Btotal_payout%5D%5Bcurrency_iso%5D=USD&order%5Btransaction%5D%5Bconfirmations%5D=0&order%5Btransaction%5D%5Bhash%5D=&order%5Btransaction%5D%5Bid%5D=569e395dd59e1c01d50004f8&order%5Buuid%5D=5a1d8dc3-e45c-56ad-bf21-b740145466c9 HTTP/1.1" 200 2195

