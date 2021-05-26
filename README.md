# ganit_assigment

Assignment
Tools and technologies used:
1.	Language: Python3.6
2.	Processing tool: Pyspark2.4
3.	Orchestrating tool: Airflow
4.	DataBase: MongoDB

Assignement contains 3 modules – 
i)	historical_data_ingestion
ii)	zip_builder
iii)	historical_data_processing

1.	historical_data_ingestion
This is a python module which downloads the currency data for past 30 days and save that data on local system in json format.

2.	 zip_builder
As python files are passed as zip to spark-submit command, so this module zips the source code before triggering the spark-submit job.

3.	Historical_data_processing
This is a pyspark module which reads the data saved by historical_data_ingestion module, processes that data, and stores raw data, cleansed data, and processed data in MongoDB.


 

As shown in image above, all the data is stored 3 different collections in a single database – ‘currency’ in MongoDB. All the collections are – 
i)	historical_data – this collection contains the raw historical data.
ii)	cleansed_historical_data – this collection contains the cleansed data after dropping duplicate data.
iii)	processed_historical_data – this collection contains the processed data after applying the filter for mentioned currencies in assignment over the cleansed data.

 
Orchestration – All the jobs are scheduled in Airflow as showing in the above image. The Dag is scheduled to run daily. 

Installation Guide
1.	Apache Airflow (in ubuntu)
i.	create virtual environment: (below command also installs python3.6)
virtualenv -p /usr/bin/python3 venv/venv_airflow_setup 

ii.	activate virtual environment:
cd /venv/venv_airflow_setup/bin
source activate	

iii.	Set the airflow home path in ~/.profile:
Sudo vim ~/.profile

 [You can also do this using command export AIRFLOW_HOME=~/airflow but you would have to export every time]

iv.	Install Airflow:
pip install apache-airflow

If it throws the "six" error while installing, then run: 
pip install apache-airflow --ignore-installed six

If it throws the “GPL library” related error while installing, then run:
export SLUGIFY_USES_TEXT_UNIDECODE=yes

v.	create user: 
airflow users create -e amit88khandelwal@gmail.com -f amit -l khandelwal -r admin -u amit 
After above command, it will ask you for password. You can set your password.

vi.	activate db: 
airflow db init

vii.	run webserver:
airflow webserver -p 8080

Webserver will ask you to login first. You can log in using the user you created in step v.

viii.	run airflow scheduler:
airflow scheduler

ix.	to create dags, create a dags directory in your airflow directory.

2.	MongoDB (Community edition)
i.	import the public key used by the package management system:
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add –

While importing public key, if it throws gnupg is not installed error. Use following command:
sudo apt-get install gnupg

After installing gnupg, retry import public key command.

ii.	Create a list file for MongoDB
Create the list file /etc/apt/sources.list.d/mongodb-org-4.4.list

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

iii.	Reload local package database
sudo apt-get update

iv.	Install the mongo packages:
sudo apt-get install -y mongodb-org

v.	Start Mongo server:
mongo

vi.	Create user in admin db:
use admin
db.createUser(
  {
    user: "ganit",
    pwd: passwordPrompt(), // or cleartext password
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
) 

3.	Pyspark

i.	Download Spark from https://spark.apache.org/downloads.html 

NOTE: choose pre-build for Apache Hadoop, click the download link and download. After installation, recommend moving the file to your home directory and maybe rename it to a shorter name such as spark. Now the spark file should be located here.
/your/home/directory/spark

ii.	Install pyspark
pip install pyspark

iii.	Set the spark home path in ~/.profile:
export SPARK_HOME="/your/home/directory/spark/python"
export PATH="$SPARK_HOME/bin:$PATH"

iv.	Check by running command:
pyspark or spark-submit
