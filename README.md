# pusher django photo feed
Building a realtime photo feed using Django and Pusher
## Getting Started
- clone this repository by running: 
```
git clone https://github.com/samuelayo/pusher_django_photo_feed.git
```
- Change directory to the cloned repo
```
cd pusher_django_photo_feed
```
- install required libraries: i.e pusher and django
```
pip install django pusher
```
- replace the XXX_APP_ID, XXX_APP_KEY, XXX_APP_SECRET and XXX_APP_CLUSTER with your own keys you obtained when you created an app on Pusher in the line below in your `photofeed\views.py` file. If you dont have a Pusher account, sign up [here](Https://pusher.com) 
```
Pusher(app_id=u'XXX_APP_ID', key=u'XXX_APP_KEY', secret=u'XXX_APP_SECRET', cluster=u'XXX_APP_CLUSTER')
```
- replace the XXX_APP_KEY and XXX_APP_CLUSTER with your app key and cluster respectively in the `feed\templates\index.html` file.

- Finally, run the application:
```
python manage.py runserver
```