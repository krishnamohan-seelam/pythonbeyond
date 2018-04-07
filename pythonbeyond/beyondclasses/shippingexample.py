from shipping import (ShippingContainer, RefrigeratedShippingContainer,
                      HeatedRefrigeratedShippingContainer)


def print_container_details(container, print_format):
    print(print_format.format(
        container.owner_code,
        container.contents,
        container.bic_code))


if __name__ == '__main__':
    container_format = "[owner_code:{0} ; contents:{1} ;bic_code:{2}]"
    emtpy_containter = ShippingContainer.create_empty("KRI", 100)
    print("Below are the empty container details")
    print_container_details(emtpy_containter, container_format)
    items_containter = ShippingContainer.create_with_items(
        "KRI", 100,
        ["laptops", "mobilephones"])
    print("Below are the items_containter details")
    print_container_details(items_containter, container_format)
    simple_containter = ShippingContainer("SWA", 100, "Footwear")
    print_container_details(simple_containter, container_format)

    empty_rfc = RefrigeratedShippingContainer.create_empty("ICE", 100,
                                                           celsius=3.0)

    print_container_details(empty_rfc, container_format)
    print("change self.bic_code = ShippingContainer.make_bic_code in base class\
,see the difference in subclass's bic_code")

    items_rfc = RefrigeratedShippingContainer.create_with_items(
        "ICE", 100,
        ["fish", "peas"], celsius=3.0)
    print("Below are the items_containter details")
    print(items_rfc)
    heatedrfc = HeatedRefrigeratedShippingContainer("HRC", 100,
                                                    "PRAWNS", celsius=-18)
