# dev engineers have access to resources

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

locals {
  services_path = "../../services"
}

module "base" {
  source = "../modules/base"
  project_id = var.project_id
  region = var.region
  name = "java-dev"
  sa_display_name = "Service Account for Java dev service"
}

module "db" {
  source = "../../modules/db"
  project_id = var.project_id
  region = var.region
  name = "db-dev"

  depends_on = [module.base]
}

module "model_api" {
  source = "../modules/model-api"
  project_id = var.project_id
  region = var.region
  name = "model-api-dev"
  sa_display_name = "Service Account for Model API"
  port =
  artifact_registry_url = module.base.artifact_registry_url

  depends_on = [modules.base]
}