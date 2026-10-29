import pytest
from electronics_store_inventory import get_inventory, add_product, update_product, delete_product


def sample_inventory():
    return {
        "P001": {
            "name": "Laptop X200",
            "category": "Laptop",
            "price": 1299.99,
            "stock": 5,
            "variants": {"color=silver": 3, "color=black": 2},
        }
    }


def test_add_product_adds_product_and_copies_variants():
    inventory = {}
    variants = {"color=black": 4}

    assert add_product(inventory, "P002", "Phone A", "Smartphone", 499.99, 4, variants)
    assert inventory["P002"] == {
        "name": "Phone A",
        "category": "Smartphone",
        "price": 499.99,
        "stock": 4,
        "variants": variants,
    }

    variants["color=white"] = 2
    assert "color=white" not in inventory["P002"]["variants"]


def test_add_product_rejects_duplicate_id():
    inventory = sample_inventory()

    assert not add_product(inventory, "P001", "Other", "Accessory", 10.0, 1, {})
    assert inventory["P001"]["name"] == "Laptop X200"


def test_update_product_changes_price_and_existing_variant_stock():
    inventory = sample_inventory()

    assert update_product(
        inventory,
        "P001",
        price=1199.99,
        variants={"color=silver": 4},
    )
    assert inventory["P001"]["price"] == 1199.99
    assert inventory["P001"]["variants"] == {"color=silver": 4, "color=black": 2}
    assert inventory["P001"]["stock"] == 6


def test_update_product_rejects_unknown_variant_without_partial_update():
    inventory = sample_inventory()
    before = {key: value.copy() if isinstance(value, dict) else value
              for key, value in inventory["P001"].items()}

    assert not update_product(
        inventory,
        "P001",
        price=1000.0,
        variants={"color=gold": 1},
    )
    assert inventory["P001"] == before


def test_update_product_rejects_unknown_product():
    assert not update_product({}, "P404", price=10.0, variants={})


def test_delete_product_removes_existing_product():
    inventory = sample_inventory()

    assert delete_product(inventory, "P001")
    assert inventory == {}


def test_delete_product_rejects_unknown_product():
    assert not delete_product(sample_inventory(), "P404")