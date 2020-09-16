#  __author__ = 'Alexey Buchkin'

import pymysql.cursors
from model.group import Group
from model.contact import Contact
import re


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_list_with_info(self):
        cursor = self.connection.cursor()
        list = []

        def clear(s):
            return re.sub("[() -]", "", s)

        def merge_phones_from_db(row):
            return "\n".join(filter(lambda x: x != "",
                                    map(lambda x: clear(x),
                                        filter(lambda x: x is not None,
                                               (row[0], row[1], row[2], row[3])))))

        def merge_emails_from_db(row):
            return "\n".join(filter(lambda x: x != "", 
                                    map(lambda x: clear(x),
                                        filter(lambda x: x is not None,
                                               (row[0], row[1], row[2])))))

        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, "
                           "phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, phone2, email, email2, email3) = row
                all_phones_from_homepage = merge_phones_from_db((home, mobile, work, phone2))
                all_emails_from_homepage = merge_emails_from_db((email, email2, email3))
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
                                    all_phones_from_homepage=all_phones_from_homepage,
                                    all_emails_from_homepage=all_emails_from_homepage))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
