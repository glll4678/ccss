dev:
	docker compose -f docker-compose.dev.yml up --build

deploy:
	docker compose up --build -d

down:
	docker compose down -v

.PHONY: dev deploy down