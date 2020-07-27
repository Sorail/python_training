#  __author__ = 'Alexey Buchkin'


def test_delete_first_group(app):
    app.group.delete_first()
