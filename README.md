# Prog-Rock

Simple example Django app using `channels` and `channels.delay` to deliver real-time progress updates over WebSockets.

## Execute

The app is configured to use `docker-compose` -- you can get it [here](https://docs.docker.com/compose/).

Once you have Docker going, then simply do the following:

```bash
docker-compose build
docker-compose run django python manage.py migrate
docker-compose up
```

The app will be live at `127.0.0.1:8000`.
