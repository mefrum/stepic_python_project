sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo nginx reload
cd /home/box/web/
sudo gunicorn -b '0.0.0.0:8080' hello:app &
cd /home/box/web/ask/
sudo gunicorn -b '0.0.0.0:8000' ask.wsgi:application &
sudo /etc/init.d/mysql start
 


