## INSTRUCTION TEXT FOR WEBSITE


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