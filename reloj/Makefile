## ----------------------------------------------------------------------
## Get data, clean everything, build the parquet storage for my watch data
## ----------------------------------------------------------------------

help:     ## Show this help.
	@sed -ne '/@sed/!s/^## //p' $(MAKEFILE_LIST) # Shows the introductory text
# Next line shows the targets nicely formatted
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Delete everything that can be regenerated
	rm -Rf input/*
	rm -Rf reloj-data/*
	@echo "CLEANED"

sourcedata: ## Get the .csv from origin write them in input/ after conversion
	@bash get-data.sh
	@echo "Data importation finished"

convert: sourcedata ## Convert input data to parquet format with partitions
	@python convert.py
	@echo "Conversion finished"

sync: ## Sincronizar con el bucket s3
	aws s3 sync --profile cjaquita reloj-data/ s3://cjbarroso-reloj-data

.DEFAULT_GOAL := help
