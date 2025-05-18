# Optional variables for manual deployment with gcloud
GCP_PROJECT_ID = your-project-id
GCP_REGION = your-region
IMAGE = us-central1-docker.pkg.dev/$(GCP_PROJECT_ID)/cloud-run-source-deploy/ml-fraud-detector

.PHONY: train run clean deploy

train:
	python app/utils/train_model.py

run:
	uvicorn app.main:app --reload

clean:
	rm -f app/model/model.pkl

deploy:
	docker build -t $(IMAGE) .
	docker push $(IMAGE)
	gcloud run deploy ml-fraud-detector \
		--image $(IMAGE) \
		--platform managed \
		--region $(GCP_REGION) \
		--allow-unauthenticated
