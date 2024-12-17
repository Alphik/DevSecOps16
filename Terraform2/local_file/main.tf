# <resource_type> <resource_name> {
#     key1 = value1
#     key2 = value2
#     ...
# }

# variable "hodi" {
#   default = "hodi1"
# }

# resource "aws_" "name" {
  
# }



resource "local_file" "file1" {
    content = "hello world"
    filename = "./testfile.txt"
    file_permission = "0440"
}

