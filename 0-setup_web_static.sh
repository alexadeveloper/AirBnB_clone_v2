#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHello world\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
content="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "37i\ $content" /etc/nginx/sites-enabled/default
sudo service nginx restart
