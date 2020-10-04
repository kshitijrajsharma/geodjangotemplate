# GeoDjango Boilerplate for Easy Project Setup
#### For Quickly Getting Started
This project includes :
1) Command for renaming project
2) Bash script of gdal and psycopg2 installation 
3) Postgres database enabled django project
4) Location as sample model and leaflet configuration for django admin

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
##### Change the GDAL verision in requirements.txt if your installed version is different from default one 
    pip install -r requirements.txt

### Download Postgres interactive installer



https://www.enterprisedb.com/downloads/postgres-postgresql-downloads




    sudo ./postgresql-10.14-1-linux-x64.run

#### Install postgis extension as well from stack builder

### Rename your project with following command
    python manage.py rename <your_current_projectname> <new_project_name> 
    eg:python manage.py rename djangoproject newproject

#### Now change your username , password and db name in settings.py accordingly to your database
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
###### For the windows user , Download and Install Anaconda Navigator , Go to environments tab , Create environment using .yaml file . Clone the repo ! You can use anaconda in ubuntu as well if you like ! 

## HURRAY !! KEEP LOVING HAI GUYS 😛    
