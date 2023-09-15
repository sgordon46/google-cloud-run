https://github.com/google-github-actions/auth#setup

export PROJECT_ID="project1-366201"
export name="sample-google-cloud-run"
export REPO="sgordon46/google-cloud-run"

gcloud iam service-accounts create "${name}" \
  --project "${PROJECT_ID}"

  #create role and attach permissions

  gcloud services enable iamcredentials.googleapis.com \
  --project "${PROJECT_ID}"

  gcloud iam workload-identity-pools create "${name}" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --display-name="${name}"

  gcloud iam workload-identity-pools describe "${name}" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --format="value(name)"

  export WORKLOAD_IDENTITY_POOL_ID="projects/917516087101/locations/global/workloadIdentityPools/sample-google-cloud-run"

  gcloud iam workload-identity-pools providers create-oidc "${name}-provider" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --workload-identity-pool="${name}" \
  --display-name="Demo provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository" \
  --issuer-uri="https://token.actions.githubusercontent.com"

  gcloud iam service-accounts add-iam-policy-binding "${name}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --project="${PROJECT_ID}" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/${WORKLOAD_IDENTITY_POOL_ID}/attribute.repository/${REPO}"

  gcloud iam workload-identity-pools providers describe "${name}-provider" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --workload-identity-pool="${name}" \
  --format="value(name)"

  #projects/917516087101/locations/global/workloadIdentityPools/sample-google-cloud-run/providers/sample-google-cloud-run-provider