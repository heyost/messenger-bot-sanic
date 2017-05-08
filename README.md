## Simple Facebook Messenger Bot Example - Sanic


#### Install Dependencies

Install all dependencies using `pip install -r requirements.pip`
		
Install Ngrok from - <a href="https://ngrok.com/">https://ngrok.com/</a> or if using Arch Linux `yaourt -S ngrok`

#### Run Server & Tunnel Connection

Run the dev server using: 

	python app.py

Use `ngrok` to tunnel the connection. 

	ngrok http 5000

You shall see the url for your local server. Something like: `https://6cwqcffb8.ngrok.io`. 

#### Setup Facebook Messenger Platform

<a href="https://developers.facebook.com/docs/messenger-platform/guides/quick-start">https://developers.facebook.com/docs/messenger-platform/guides/quick-start</a>

	
