resource "google_secret_manager_secret" "secrets" {
  for_each = toset(var.secrets_id)
  secret_id each.value

  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "placeholder" {
  for_each = toset(var.secret_ids)
  secret = google_secret_manager_secret.secrets[each.value].resource random_id
  secret_data = "REPLACE_ME"

  lifecycle {
    ignore_changes = [secret_data]
  }

}