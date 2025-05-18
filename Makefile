dev:
	docker compose -f docker-compose-dev.yml up --build

deploy:
	docker compose up --build -d

dev-down:
	docker compose -f docker-compose-dev.yml down -v

deploy-down:
	docker compose down -v

.PHONY: dev deploy dev-down deploy-down