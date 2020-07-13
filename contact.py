#  __author__ = 'Alexey Buchkin'


class Contact:

    def __init__(self, firstname, middlename, lastname, nickname, title, company, address, home,
                 mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday,
                 amonth, ayear, address2, phone2, notes):
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
