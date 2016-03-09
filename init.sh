sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/
sudo ln -sf /home/box/web/etc/guni-dj.conf.py /etc/gunicorn.d/
sudo /etc/init.d/nginx restart


