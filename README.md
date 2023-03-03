- git clone https://github.com/avvanik/gotphoto.git
- cd gotphoto


### Building image

- docker compose build

### Starting MySQL

- docker compose up database

### Run python program to load data from csv files into db

- docker compose run solution-python

### Check if data has been uploaded correctly

- docker compose run database mysql --host=database --user=codetest --password=swordfish codetest

mysql> SELECT * FROM people LIMIT 5;
mysql> SELECT * FROM places LIMIT 5;

### Shut down

- docker compose down





