echo "BUILD START"
/usr/bin/python -m ensurepip
/usr/bin/python -m pip install --upgrade pip
/usr/bin/python -m pip install -r requirements.txt
/usr/bin/python manage.py collectstatic --noinput --clear
echo "BUILD END"
