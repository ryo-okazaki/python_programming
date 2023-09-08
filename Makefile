build:
	docker-compose up -d --build

down:
	docker-compose down

reboot:
	docker-compose down
	docker-compose up -d --build

interactive:
	docker-compose exec anaconda bash

db:
	docker-compose exec mysql mysql -u root -p

memcache:
	docker-compose exec memcached memcached -vv