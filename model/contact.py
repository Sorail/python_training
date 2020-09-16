#  __author__ = 'Alexey Buchkin'

from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None,
                 phone2=None, notes=None, id=None, all_phones_from_homepage=None, all_emails_from_homepage=None,
                 group=None):
        self.notes = notes
        self.phone2 = phone2
        self.address2 = address2
        self.ayear = ayear
        self.amonth = amonth
        self.aday = aday
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.homepage = homepage
        self.email3 = email3
        self.email2 = email2
        self.email = email
        self.fax = fax
        self.work = work
        self.mobile = mobile
        self.home = home
        self.address = address
        self.company = company
        self.title = title
        self.nickname = nickname
        self.lastname = lastname
        self.middlename = middlename
        self.firstname = firstname
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage
        self.group = group

    def __repr__(self):
        return "id:%s;firstname:%s;middlename:%s;lastname:%s;home:%s;" \
               "mobile:%s;work:%s;phone2:%s;email:%s;email2:%s;email3:%s;" \
               "all_phones_from_homepage:%s;all_emails_from_homepage:%s" % \
               (self.id, self.firstname, self.middlename, self.lastname, self.home, self.mobile, self.work, self.phone2,
                self.email, self.email2, self.email3, self.all_phones_from_homepage, self.all_emails_from_homepage)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname \
               and ((self.all_phones_from_homepage is None and other.all_phones_from_homepage is None)
                    or (self.all_phones_from_homepage == other.all_phones_from_homepage)) \
               and ((self.all_emails_from_homepage is None and other.all_emails_from_homepage is None)
                    or (self.all_emails_from_homepage == other.all_emails_from_homepage))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
