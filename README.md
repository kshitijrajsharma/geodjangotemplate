# GeoDjango Boilerplate for Easy Project Setup
#### For Quickly Getting Started
This project includes :
1) Command for renaming project
2) Bash script of gdal and psycopg2 installation 
3) Postgres database enabled django project
4) Location as sample model and leaflet configuration for django admin
5) Django-restframework-GIS with sample model and Geojson API view
6) Django Rest Swagger

### Install Python3, pip and virtualenv first
##### Skip this, step if you already have one

    sudo apt-get install python3
    sudo apt-get install -y python3-pip
    sudo apt install python3-virtualenv
##### Create your virtual env
    virtualenv myenv
    source ./myenv/bin/activate
### Clone this repo
    git clone https://github.com/itskshitiz321/geodjangotemplate.git
##### Navigate to this repo 
    chmod +x library.sh
    ./library.sh
    ogrinfo --version
##### Change the GDAL verision in requirements.txt if your installed version is different from default one (gdal version can be checked from previous command ogrinfo--version
    pip install -r requirements.txt

### Download Postgres interactive installer



https://www.enterprisedb.com/downloads/postgres-postgresql-downloads



##### Now change the postgresql version that you have downloaded and run this command

    chmod +x ./postgresql-10.14-1-linux-x64.run
    sudo ./postgresql-10.14-1-linux-x64.run

#### Install postgis extension as well from stack builder

### Rename your project with following command
    python manage.py rename <your_current_projectname> <new_project_name> 
    eg:python manage.py rename djangoproject newproject

#### Now change your username , password and db name in settings.py accordingly to your database
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
### For Anaconda User
    conda env create -f environment.yml
##### Now follow from renaming the project

