# Errata

## S. 123, Mitte
Hier steht:

"Im Hinblick auf Vergleichsoperatoren und logische Operatoren ist es wichtig zu wissen, dass eine aus der Mathematik bekannte Kettenoperation wie _a < b < c_
in Python nicht funktioniert. Sie muss in _a < b and b < c_ unterteilt werden."

Das stimmt nicht. In den meisten Programmiersprachen ist eine solche Verkettung von Vergleichsoperatoren tatsächlich unzulässig, in Python jedoch nicht.
