build:
	docker-compose up -d --build

down:
	docker-compose down

interactive:
	docker-compose exec anaconda bash

db:
	docker-compose exec mysql mysql -u root -p