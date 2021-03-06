# wget https://raw.githubusercontent.com/drandreaskrueger/buyme/master/_how-to/restart_production.sh
# dos2unix restart_production.sh
# chmod 700 restart_production.sh
# ./restart_production.sh

rm buyme_production -rf

mkdir buyme_production
cd buyme_production

git clone -b production https://github.com/drandreaskrueger/buyme.git
cd buyme

python manage.py makemigrations buyme
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser

git update-index --assume-unchanged buyme/configPrivate.py

echo .
echo . You must edit configPrivate.py and then start the server:
echo . nano buyme/configPrivate.py
echo . python manage.py runserver 0.0.0.0:8001
echo .

