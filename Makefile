.PHONY: build, dev, run

build:
	@docker build -t bookshelf_dev .


# Change to Docker compose
# dev:
# 	@docker run --name bookshelf_dev --rm -it -v $(shell pwd):/app localhost/bookshelf_dev:latest

# run:
# 	@docker run --name bookshelf_dev --rm -it -v $(shell pwd):/app -p 5000:5000 localhost/bookshelf_dev:latest