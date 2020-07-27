#  __author__ = 'Alexey Buchkin'


def test_delete_first_contact(app):
    app.contact.delete_first_contact()
