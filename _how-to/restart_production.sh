# wget this
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
python manage.py runserver --insecure 0.0.0.0:8001

