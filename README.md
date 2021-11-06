# Telegram-Bot-Demo
This is Demo Telegram Bot created by Nicholas using python-telegram-bot

# web hooks notes for heoku deployment
in your procfile:
change worker: python <script.py>
into web: python <script.py>
heroku only starts a webnserver when your procfile declares a web dyno.

good luck

Edit: Clarification.
Heroku always has a webserver running, but it does not assign a port to a process that's not declared web. Because of this the python script cannot bind to a port and hence does not start the webserver.
Heroku will not route any traffic to your app because of this.
Indeed in the example in the wiki it uses port 0.0.0.0, wich it should be.

Our examples usually start the bot using Updater.start_polling. This method uses the getUpdates API method to receive new updates for your bot. This is fine for smaller to medium-sized bots and for testing, but if your bot receives a lot of traffic, it might slow down the response times.

## get webhookinfo
https://api.telegram.org/bot<ID>:<APIKEY>/getWebhookInfo
