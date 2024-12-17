resource "local_file" "file2" {
    filename = "./${var.file_name}"  # -> "./test2.txt"
    content = var.file_content #this is my 2 nd test
    file_permission = "0${var.file_permission}"
}