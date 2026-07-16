# Project Managers have access to resources

terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "> 5.0.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region = var.region
}

module "base" {
  source = "../../modules/base"
  project_id = var.project_id
  region = var.region
  name = "java-staging"
  sa_display_name = "Service Account for Java staging service"
}

module "db" {
  source = "../../modules/db"
  project_id = var.project_id
  region = var.region
  name = "db-staging"

  depends_on = [module.base]
}

module "model_api" {
  source = "../modules/model-api"
  project_id = var.project_id
  region = var.region
  name = "model-api-staging"
  sa_display_name = "Service Account for Model API"
  port =
  artifact_registry_url = module.base.artifact_registry_url

  depends_on = [modules.base]
}