## INSTRUCTION TEXT FOR WEBSITE


### FACEBOOK SETUP

1. Set up a facebook [page](https://www.facebook.com/pages/create/).

2. Go to the Facebook Developer’s Quickstart Page and click “Skip and Create App ID” at the top right. Then create a new Facebook App for your bot and give your app a name, category and contact email.
    
	![create-fb-app](https://blog.hartleybrody.com/wp-content/uploads/2016/06/create-fb-app-1024x604.png "")
    
    You’ll see your new App ID at the top right on the next page. Scroll down and click “Get Started” next to Messenger.
    
    ![setup-fb-messenger-app](https://blog.hartleybrody.com/wp-content/uploads/2016/06/setup-fb-messenger-app-1024x613.png "")


3. Now you’re in the Messenger settings for your Facebook App. There are a few things in here you’ll need to fill out in order to get your chatbot wired up to the Heroku endpoint we setup earlier.

	![setup-fb-messenger-app](https://blog.hartleybrody.com/wp-content/uploads/2016/06/page-access-token-generation-1024x346.png "")
    
    Using the Page you created earlier (or an existing Page), click through the auth flow and you’ll receive a Page Access Token for your app.
        
	Click on the Page Access Token to copy it to your clipboard. 
   
4. Paste the page access token into its field in the config.py file.

5. Head over to Messenger under products in you projects facebook developer page and click on settings. Navigate to the webhooks section, click on edit events and select messages and messaging_postbacks as shown below.
	
	![fb-events](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/events.png "")



### NGROK SETUP

1. Download your desired bot template from the website

2. Dowload ngrok from their [page](https://ngrok.com/download).

3. On Linux or OSX you can unzip ngrok from a terminal with the following command. 

	```
	unzip /path/to/ngrok.zip

	```
	On Windows, just double click ngrok.zip.

4. Navigate to the folder containing the unzipped contents of ngrock and run it with the command ./ngrok . You should see something similar to the image below on your terminal.

5. Copy and replace the facebook token and server url in the config.py file and replace FACEBOOK_TOKEN_HERE with the facebook page token selected as in the instructions above and SERVER_URL_HERE with the url displayed after running ngrok:

	```
	CONFIG = {
     'FACEBOOK_TOKEN': 'FACEBOOK_TOKEN_HERE',
     'VERIFY_TOKEN': 'my_verify_token',
     'SERVER_URL': 'SERVER_URL_HERE'
 	}

	```

6. Run your bot by running python server.py after saving your changes to the server.py file. 

7. Head over to your apps page on the Facebook for Developers site and under products, select webhooks.

	![URL subscription](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/subscription.png "")

	Once selected click on edit subscription and copy your https url (as shown below) from ngrock in your terminal to the Callback URL section followed by /webhook. 
	
	![ngrok](https://cdn-images-1.medium.com/max/1600/1*LtnvanCk2-ZVJY1kA0cMfQ.png "")
	
	According to the image above, our callback url will be 

	```
	https://bd2cb171.ngrok.io/webhook

	```
	Under the Verify Token field of the page subscription, add 
	```
	my_verify_token

	```
	as seen in the config.py file. 
	
	![Webhook](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/webhook.png "")
	
	You can then click on the verify and save button to save the webhook.


### HEROKU INSTRUCTIONS

After clicking the click to deploy buttons below, your selected template will be hosted and deployed ontu Heroku automatically. The only issue is that the config.py file does not contain your specific Facebook page keys and server url.

To fix this, follow the following steps;

1. Dowload the heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli). 

2. Once heroku has been installed, open the heroku [dashboard](https://dashboard.heroku.com/apps).
Select your newly created app and navigate to the deploy section as shown in the images below.

![Overview](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/overview.png "").


![Deploy](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/deploy.png "")

3. Run the code indicated in the image below to get a copy of your bot template and navigate to its folder in your terminal.

![Run](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/install-amended.png "")


4. Open your config.py file and fill in the required variables replacing FACEBOOK_TOKEN_HERE with you facebook app pages' token and SERVER_URL_HERE with the url of your newly created heroku server.

The config.py file should look like the snippet below:

	```
	CONFIG = {
     'FACEBOOK_TOKEN': 'FACEBOOK_TOKEN_HERE',
     'VERIFY_TOKEN': 'my_verify_token',
     'SERVER_URL': 'SERVER_URL_HERE'
 	}

	```

When filled, it should look like the snippet below:

	```
	CONFIG = {
     'FACEBOOK_TOKEN': 'EAAHUC2GIMSoZAioyW4orexO9tCCHvdCCnC2GIMSoZAioyW4orexO9tCCHvdCC2GIMSoZAioyW4orexO9tCCHvdCLF1mFlnqC2GIMSoZAioyW4orexO9tCCHvdCxdLF1mFlnqC2GIMSoZAioyW4orexO9tCCHvdC',
     'VERIFY_TOKEN': 'my_verify_token',
     'SERVER_URL': 'https://site-example-name.herokuapp.com/'
 	}
 	
	```

5. Once filled, save your config.py file and head over to the heroku [dashboard](https://dashboard.heroku.com/apps) and select your previously created app. 

6. Once selected you should se something similar to the image below: 

![Overview](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/overview.png "").

Navigate to the deploy section and then select the heroku-git option as shown in the image below:

![Deploy](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/deploy.png "")

Ensure you have navigated to the folder containing your bot and type in the given commands to your terminal as indicated in the image below:

![Install](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/install.png "")


## HOW TO EDIT YOUR BOTS TEMPLATE

The logic of all the bots here are held in the messenger.py file of the template. Below are the following elements you'll want to add followed by the code needed to implement them.

### QUICK REPLIES

A quick reply consists of small buttons which are good for presenting multiple choices to a user. A quick reply is defined in own function as shown below:

```
def hello(recipient):
    page.send(recipient, "Hi! 😄")
    page.send(recipient, "What would you like to buy?",
              quick_replies=[QuickReply(title=("Sneakers 👟"), payload="BUY_SNEAKERS"),
                             QuickReply(title=("Jeans 👖"), payload="BUY_JEANS"),
                             ],
              metadata="DEVELOPER_DEFINED_METADATA")
	      
```

![quick reply](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/quick_reply.png "")


The response for the button is ran when the payload is recieved. The Jeans 👖 button above should allow the user to view all the jeans and make a purchase. The template is called when the payload BUY_JEANS from button above, is recieved as shown below.

```
elif quick_reply_payload == 'BUY_JEANS':
            show_jeans(sender_id)
            start_again(sender_id)
   
```

This snippet is found within the recieved message function which collects the different messages and deals with them respectively.

```
@page.handle_message
def received_message(event):
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_message = event.timestamp
    message = event.message
    
```

Running both functions produces the result shown below:

![quick_resuts](https://github.com/anthonymiyoro/Bot-Builder-Site/blob/master/images/quick_reply_results.png "")







