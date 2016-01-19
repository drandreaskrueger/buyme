# wget https://raw.githubusercontent.com/drandreaskrueger/buyme/master/_how-to/restart.sh; dos2unix restart.sh ; chmod 700 restart.sh ; ./restart.sh

rm buyme -rf

git clone https://github.com/drandreaskrueger/buyme.git
cd buyme

python manage.py makemigrations buyme
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser

git update-index --assume-unchanged buyme/configPrivate.py

echo .
echo . You must edit configPrivate.py and then start the server:
echo .
echo . cd buyme 	
echo . nano buyme/configPrivate.py
echo . python manage.py runserver 0.0.0.0:8000
echo .


