class InvalidData(Exception):
    pass

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email

    @property
    def jmeno(self):
        return self._jmeno
    
    @jmeno.setter
    def jmeno(self, jmeno):
        if not any(znak.isalpha() for znak in jmeno):
            raise InvalidData("Jmeno musi obsahovat alespon jedno pismeno")
        for znak in jmeno:
            if not (znak.isalpha() or znak.isspace()):
                raise InvalidData("Jmeno muze obsahovat jen pismena a mezery")
        self._jmeno = jmeno

    @property
    def telefon(self):
        return self._telefon
    
    @telefon.setter
    def telefon(self, telefon):
        if not (telefon.startswith('+')):
            raise InvalidData("Telefonni cislo musi zacinat '+' a obsahovat 12 cislic")
        if not (len(telefon) == 13):
            raise InvalidData("Telefonni cislo musi obsahovat 12 cislic")
        if not telefon[1:].isdigit():
            raise InvalidData("Telefonni cislo musi obsahovat 12 cislic")
        self._telefon = telefon

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if not ("@" in email):
            raise InvalidData("Email musi obsahovat zavinac, pismenka a koncit na .cz")
        if not (email.endswith('.cz')):
            raise InvalidData("Email musi koncit na .cz")
        email2 =email.replace('.', '')
        email2 = email2.replace('@', '')
        if not email2.isalpha():
            raise InvalidData("Email musi obsahovat zavinac, pismenka a koncit na .cz") 
        self._email = email

    def __str__(self):
        return f"Osoba(jmeno={self.jmeno}, telefon={self.telefon}, email={self.email})"

if __name__ == "__main__":
    try:
        test = Osoba("Jan Novák", "+420123456789", "honza@seznam.cz")
        print(f"✓ Validní: {test}")
    except InvalidData as e:
        print(f"✗ Chyba: {e}")


