# a place for shared resources across environments

resource "google_service_account" "sa" {
  account_id = "${var.name}-sa"
  display_name = var.sa_display_name
}

resource "google_project_service" "artifactregistry" {
  service = "artifactregistry.googleapis.com"
}

resource "google_cloud_run_v2_service" "service" {
  name = "${var.name}-service"
  location = var.region

  template {
    service_account = google_service_account.sa.email
    containers {
      image = "${var.artifact_registry_url/${var.name}:latest"

      ports {
        container_port = var.port
      }
    }
  }

}