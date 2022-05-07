.PHONY: build
build: dependencies
	@echo "Building..."
	@rm -rf *.zip
	@zip -r demo_module.zip *
	@echo "Built."

requirements.txt:
	touch requirements.txt

dependencies:
	mkdir -p ./dependencies
	pip install -r requirements.txt --target ./dependencies
