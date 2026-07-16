# a place for shared resources across environments

resource "google_project_service" "artifactregistry" {
  service = "artifactregistry.googleapis.com"
}

