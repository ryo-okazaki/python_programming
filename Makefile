build:
	docker-compose up -d --build

down:
	docker-compose down

interactive:
	docker-compose exec anaconda bash