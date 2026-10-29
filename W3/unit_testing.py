
# Opmerking: De aanpak die hier wordt laten zien, is een eenvoudige introductie in unit testen. 
# Later zal je meer diepgaande technieken leren met behulp van de ingebouwde frameworks en libraries van Python

contacts = []

def add_contact(name, phone_number, email):
    contact = {
        'name': name,
        'phone_number': phone_number,
        'email': email
    }
    contacts.append(contact)

def search_by_name(name):
    return list(filter(lambda c: name.lower() in c['name'].lower(), contacts))

def delete_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)

def test():
    # Test adding a contact
    add_contact('John Doe', '06876543210', 'john@hotemail.com')
    # Let's check if the function works correctly
    assert len(contacts) == 1
    assert contacts[0] == {
        'name': 'John Doe',
        'phone_number': '06876543210',
        'email': 'john@hotemail.com'
    }

    # Test searching contacts
    search_results = search_by_name("John")
    # Let's check if the function works correctly
    assert len(search_results) == 1
    assert search_results[0]['name'] == 'John Doe'

    # Test deleting a contact
    delete_contact("John Doe")
    # Let's check if the function works correctly
    assert len(contacts) == 0
    assert search_by_name("John") == []

    print("All tests are executed.")

test()
