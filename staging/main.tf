resource "random_pet" "server" {
  keepers = {
    # Generate a new pet name each time we switch to a new AMI id
    test = local.test
  }
}
