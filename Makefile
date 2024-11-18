set-project:
	gcloud config set project data-lake-raw-development

enable-services:
	gcloud services enable run.googleapis.com
	gcloud services enable cloudbuild.googleapis.com

build:
	gcloud builds submit --tag gcr.io/data-lake-raw-development/doubles-drawer

deploy:
	gcloud run deploy doubles-drawer \
		--image gcr.io/data-lake-raw-development/doubles-drawer \
		--platform managed \
		--allow-unauthenticated \
		--region us-central1

run-services:
	gcloud run services add-iam-policy-binding doubles-drawer \
		--member="allUsers" \
		--role="roles/run.invoker" \
		--region us-central1 \
		--platform managed

up:
	python3 app.py