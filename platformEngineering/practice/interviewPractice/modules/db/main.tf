
resource "google_service_account" "sa" {
  account_id = "${var.name}-sa"
  display_name = var.sa_display_name
}

resource "google_sql_database" "database" {
  name = "${var.name}-database"
  instance = google_sql_database_instance.instance.name
}

resource "google_sql_database_instance" "instance" {
  name = "${var.name}-database-instance"
  region = var.region
  database_version = ""
}

