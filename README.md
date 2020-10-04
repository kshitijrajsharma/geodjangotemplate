# geodjangotemplate
### Install Python first


    sudo apt-get install python3


### Install Pip


    sudo apt-get install -y python3-pip

### Install virtualenv



    sudo apt install python3-virtualenv


### Create your virtual env


    virtualenv myenv
    source ./myenv/bin/activate
### Clone this repo 
#### Navigate to this repo 
    chmod +x <library.sh>
    ./library.sh
    ogrinfo --version
### Change the GDAL verision in requirements.txt if your installed version is different from default one 
    pip install -r requirements.txt

### Download Postgres interactive installer



https://www.enterprisedb.com/downloads/postgres-postgresql-downloads




    sudo ./postgresql-10.14-1-linux-x64.run

### Install postgis extension as well from stack builder



#### Now change your username , password and db name with your postgres database 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
