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

