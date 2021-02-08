
.PHONY: run
run: build init start

.PHONY: init
init:
	docker run \
	-it --rm -v $(PWD):/home \
	parkeraddison/netem-init \
	python tool/setup/build_compose.py \
	-s tool/ -c config/tool.json -e $(PWD)/.env -o $(PWD)/data/

.PHONY: build
build:
	$(MAKE) -C tool build

.PHONY: start
start:
	$(MAKE) -C tool raw

.PHONY: stop
stop:
	$(MAKE) -C tool stop

.PHONY: down
down:
	$(MAKE) -C tool down
