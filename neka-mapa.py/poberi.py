import orodja
import re
import requests

STEVILO_STRANI =21

vzorec = (
    r'class="GO-Results-Naziv bg-dark px-3 py-2 font-weight-bold text-truncate text-white text-decoration-none">\s*'
    r'<span>(?P<Znamka>\S+)\s*(?P<Model>.*?)</span>.*?'
    r'<td class="w-25 d-none d-md-block pl-3">1.registracija</td>\n\n\s*<td class="w-75 pl-3">(?P<Prva>\d+?)</td>.*?'
    r'<td class="pl-3">(?P<prevozeni>\d*) km</td>.*?'
    r'<td class="d-none d-md-block pl-3">Gorivo</td>.*?'
    r'<td class="pl-3">(?P<gorivo>.*?)</td>.*?' #gorivo
    r'<td class="d-none d-md-block pl-3">Menjalnik</td>.*?<td class="pl-3 text-truncate">(?P<menjalnik>.*?)</td>.*?' #menjalnik
    r'<td class="d-none d-md-block pl-3">Motor</td>.*?<td class="pl-3 text-truncate">\n\n\s*(?P<motor>.*?)\n\n\s*</td>.*?' #motor
    r'<div class="GO-Results-*?-Price-TXT-.*?">(?P<cena>\d.*?)\s' #cena
)


najdeni_filmi = 0

for stran in range(STEVILO_STRANI):
    stran += 1
    url = f'https://www.avto.net/Ads/results.asp?znamka=&model=&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=&cenaMin=0&cenaMax=999999&letnikMin=0&letnikMax=2090&bencin=0&starost2=999&oblika=11&ccmMin=0&ccmMax=99999&mocMin=&mocMax=&kmMin=0&kmMax=9999999&kwMin=0&kwMax=999&motortakt=0&motorvalji=0&lokacija=0&sirina=0&dolzina=&dolzinaMIN=0&dolzinaMAX=100&nosilnostMIN=0&nosilnostMAX=999999&lezisc=&presek=0&premer=0&col=0&vijakov=0&EToznaka=0&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1110100020&EQ8=1010000001&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PSLO=&akcija=0&paketgarancije=&broker=0&prikazkategorije=0&kategorija=0&zaloga=10&arhiv=0&presort=3&tipsort=DESC&stran={stran}'
    datoteka = f'Avti-str={stran}.html'
    orodja.shrani_spletno_stran(url, datoteka)
    vsebina = orodja.vsebina_datoteke(datoteka)

    with open('test.html', 'a', encoding='utf-8') as f:
        for zadetek in re.finditer(vzorec, vsebina, flags=re.DOTALL):
            print(zadetek.groupdict(), file=f, end=",\n")
            najdeni_filmi += 1
    

print(najdeni_filmi)