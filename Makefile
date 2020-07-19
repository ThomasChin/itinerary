compose_file := docker-compose.dev.yml
compose := docker-compose -f $(compose_file)

.PHONY: black
black:
	$(compose) exec web black .

.PHONY: build
build:
	$(compose) build $(name)

.PHONY: clean
clean:
	rm -rf .docker-data/

.PHONY: create_superuser
create_superuser:
	$(compose) exec web python manage.py createsuperuser

.PHONY: dbfresh
dbfresh: down clean up pg_isready migrate loaddevdata

.PHONY: down
down:
	$(compose) down

.PHONY: exec
exec:
	$(compose) exec $(name) $(c)

.PHONY: refresh
refresh: down clean build up pg_isready migrate loaddevdata

.PHONY: make_migrations
make_migrations:
	$(compose) exec web python manage.py makemigrations

.PHONY: migrate
migrate:
	$(compose) exec web python manage.py migrate

.PHONY: pg_isready
pg_isready:
	$(compose) exec db /bin/sh -c "until pg_isready; do sleep 2 ; done; sleep 2"

.PHONY: up
up:
	$(compose) up -d

.PHONY: datadump
datadump:
	$(compose) exec web python manage.py dumpdata --indent 2 --exclude auth.permission --exclude contenttypes --output dump.json \

.PHONY: loaddevdata
loaddevdata:
	$(compose) exec web python manage.py loaddata fixture.json

.PHONY: pytest
pytest:
ifeq ($(strip $(TEST)),)
	$(compose) exec web pytest -c pytest.ini .
else
	$(compose) exec web pytest -c pytest.ini . -k $(TEST)
endif
