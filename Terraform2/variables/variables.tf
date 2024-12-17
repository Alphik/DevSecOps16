variable "file_name" {
  type = string
  default = "test2.txt"
}
variable "file_content" {
    type = string
    description = "this var contains the content of the file"
    default = "this is my 2 nd test"
}
variable "file_permission" {
    type = number
    default = 777
}