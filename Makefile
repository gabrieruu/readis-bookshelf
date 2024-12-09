.PHONY: dev, build

dev:
	@docker run --name bookshelf_dev --rm -it -v /Users/gsantos/code/github/gabrieruu/bookshelf:/app localhost/bookshelf_dev:latest

build:
	@docker build -t bookshelf_dev .