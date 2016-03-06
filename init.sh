sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/
sudo /etc/init.d/nginx restart


