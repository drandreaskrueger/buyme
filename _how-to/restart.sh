# wget this
# chmod 700 restart.sh
# ./restart.sh

rm buyme -rf
git clone https://github.com/drandreaskrueger/buyme.git
cd buyme
python manage.py makemigrations buyme
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8001

