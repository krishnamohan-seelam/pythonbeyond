from shipping import ShippingContainer


def print_container_details(container,print_format):
      print(print_format.format(
        container.owner_code,
        container.contents,
        container.bic_code))


if __name__ == '__main__':
    container_format ="[owner_code:{0} ; contents:{1} ;bic_code:{2}]"
    emtpy_containter = ShippingContainer.create_empty("KRI")
    print("Below are the empty container details")
    print_container_details(emtpy_containter,container_format)
    items_containter = ShippingContainer.create_with_items(
        "KRI",
        ["laptops","mobilephones"])
    print("Below are the items_containter details")
    print_container_details(items_containter,container_format)
    simple_containter = ShippingContainer("SWA","Footwear")
    print_container_details(simple_containter,container_format)
  