output "my_new_file_id" {
  value = local_file.test3.id
}

output "read_file_content" {
  value = data.local_file.read_file.filename
}
output "read_file_base64" {
  value = "${data.local_file.read_file.content_base64} --- ${data.local_file.read_file.content_base64sha256}"
}

output "tiktok" {
    value = data.local_file.tiktok_trends.content
}