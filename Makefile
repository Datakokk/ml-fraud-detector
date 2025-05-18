# Optional variables for manual deployment with gcloud
GCP_PROJECT_ID = your-project-id
GCP_REGION = your-region

.PHONY: train run clean deploy

# Trains the model and saves model.pkl in app/model/
train:
	python app/utils/train_model.py

# Runs the microservice locally with Uvicorn
run:
	uvicorn app.main:app --reload

# Removes the model and temporary files
clean:
	rm -f app/model/model.pkl

# Manually deploy to Cloud Run (if not using GitHub Actions)
deploy:
	gcloud builds submit --tag gcr.io/$(GCP_PROJECT_ID)/ml-fraud-detector
	gcloud run deploy ml-fraud-detector \
		--image gcr.io/$(GCP_PROJECT_ID)/ml-fraud-detector \
		--platform managed \
		--region $(GCP_REGION) \
		--allow-unauthenticated
