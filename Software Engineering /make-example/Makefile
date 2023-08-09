.PHONY: all read_clean_data model analysis

all: analysis

read_clean_data:
	python read_clean_data.py

model: read_clean_data
	python model.py

analysis: model
	python analysis.py

.PHONY: clean
clean:
	rm -f clean_data.csv lam.pickle train_data.csv test_data.csv forecasts.csv
