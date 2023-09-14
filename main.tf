#export GOOGLE_APPLICATION_CREDENTIALS="/Users/sgordon/credentials/project1-366201-179592c1146e.json"

# terraform {
#   required_version = ">= 1.3"

#   required_providers {
# 	google = ">= 3.3"
#   }
# }


provider "google" {
  region = "us-central1"
  zone    = "us-central1-a"
  project = "project1-366201"
}



resource "google_cloud_run_v2_service" "default" {
  name     = "my-tomcat-2023"
  location = "us-central1"

  template {
    containers {
      image = "us-central1-docker.pkg.dev/project1-366201/my-tomcat-2023/my-tomcat-image-2023:latest"
    }
  }
}

resource "google_cloud_run_service_iam_binding" "default" {
  location = google_cloud_run_v2_service.default.location
  service  = google_cloud_run_v2_service.default.name
  role     = "roles/run.invoker"
  members = [
    "allUsers"
  ]
}


output "URL" {
  description = "Google Cloud Run Url"
  value = google_cloud_run_v2_service.default.uri
}
