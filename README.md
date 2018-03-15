# BUILD A PHOTO FEED USING DJANGO

Here, we will learn about building a photo feed using Django. This is similar to instagram, but a stripped off version without the comments and like feature. The full tutorial can be found here : [https://pusher.com/tutorials/photo-feed-django/ ](https://pusher.com/tutorials/photo-feed-django/) 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

- Clone this repository by running: 
```
git clone https://github.com/samuelayo/pusher_django_photo_feed.git
```
- Change directory to the cloned repo
```
cd pusher_django_photo_feed
```
- Install required libraries: i.e pusher and django
```
pip install django pusher
```

### Prerequisites

#### Setup Pusher

- Replace the XXX_APP_ID, XXX_APP_KEY, XXX_APP_SECRET and XXX_APP_CLUSTER with your own keys you obtained when you created an app on Pusher in the line below in your `photofeed\views.py` file. If you dont have a Pusher account, sign up [here](Https://pusher.com) 
```
Pusher(app_id=u'XXX_APP_ID', key=u'XXX_APP_KEY', secret=u'XXX_APP_SECRET', cluster=u'XXX_APP_CLUSTER')
```
- Replace the XXX_APP_KEY and XXX_APP_CLUSTER with your app key and cluster respectively in the `feed\templates\index.html` file.


#### Database Migrations
 - Run the following command at the root of your application to  make the migrations needed for the database
 
 ```
 python manage.py makemigrations
 ```
 
 - Run this command to migrate the database
 
 ```
  python manage.py migrate
 ```

And finally, start the application:

```
python manage.py runserver.
```
and visit http://localhost:8000/ to see the application in action.
## Built With

* [Pusher](https://pusher.com/) - APIs to enable devs building realtime features
* [DJango](https://docs.djangoproject.com/) - The web framework for perfectionists with deadlines. 
* [Jquery](https://jquery.com/) - The Write Less, Do More, JavaScript Library

