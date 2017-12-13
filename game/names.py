
lista = [
    "Anna","Maria","Krystyna","Barbara","Teresa","Elżbieta","Zofia","Ewa",
    "Jadwiga","Sylwia","Halina","Danuta","Małgorzata","Gosia","Helena","Grażyna",
    "Bożena","Stanisława","Jolanta","Jola","Urszula","Wanda","Ula","Ala",
    "Alicja","Dorota","Agnieszka","Beata","Katarzyna","Joanna","Asia","Renata",
    "Iwona","Aleksandra","Ola","Genowefa","Hanna","Alina","Józefa","Monika",
    "Monia","Marta","Martyna","Marzena","Izabela","Iza","Emila","Agata",
    "Edyta","Aniela","Wioletta","Wiola","Justyna","Aga","Zuzanna","Zuza",
    "Natalia","Wiktoria","Karolina","Róża","Ilona","Julia","Anita","Ewelina",
    "Magda","Kamila","Paulina","Patrycja","Eliza","Michalina","Adamia","Janina",
    "Honorata","Bernarda","Bernadetta","Faustyna","Fiona","Violetta","Viola","Kasia",
    "Ania","Ela","Irena","Celina","Felicja","Frnciszka","Olga","Zosia",
    "Izabella",
]
#zrobie to na wątkach, obiecuje
def correct_name(name):
	if name.endswith("a"):
            for buff_name in lista:
                if buff_name == name:
                    return True
            return False
	else:
		return False