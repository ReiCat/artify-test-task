# artify-test-task

1. Create database & user with password

`$ sudo mysql`

`mysql> CREATE USER 'artify'@'localhost' IDENTIFIED BY 'artify';`

`mysql> GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'artify'@'localhost' WITH GRANT OPTION;`

`mysql> exit`

Login to your newly created account to see it was created:

`$ mysql -u artify -p`

Create database:

`mysql> CREATE DATABASE artify;`

2. Create virtual environment for the project
* It is assumed you have virtualenv installed globally

`$ virtualenv -p python3 venv`

3. Activate it

`$ source venv/bin/activate`

4. Install all the requirements

`$ pip install -r requirements.txt`

5. Create .env file and add database dsn

`$ touch .env && echo "DATABASE_URL=mysql+pymysql://artify:artify@127.0.0.1/artify" >> .env`

6. Run migrations

`$ make migrate-up`

7. Build templates

`$ make templates-build`

8. Run the server

`$ make run`