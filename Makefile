OS_NAME := $(shell uname)

main: run_nginx_docker

# ---- Initialization ----------------------------------------------------------

run_nginx_docker:
	docker run --name nginx -v $(PWD):/usr/share/nginx/html/ -p 80:80 -d nginx

# ---- Parser ------------------------------------------------------------------

# make telong <ISBN-13>
#
# https://stackoverflow.com/a/6273809/686105

telong:
	-python3 tenlong.py $(filter-out $@,$(MAKECMDGOALS))

%:
	@:

# ---- Run ---------------------------------------------------------------------

run: review_serve

review_html:
ifeq (${OS_NAME}, Darwin)
	open index.html
else
	firefox index.html
endif

review_serve:
ifeq (${OS_NAME}, Darwin)
	open http://localhost
else
	firefox http://localhost
endif

# ---- Clean -------------------------------------------------------------------

clean:
	- docker rm -f nginx
	-rm -f *.html
