import orodja
import ast


def funkcija1(vhodna, izhodna):
    '''v datoteki slovarjev olepsa model, znamko in motor  '''
    with open(vhodna, 'r', encoding='utf-8') as s:
        with open(izhodna, 'w', encoding='utf-8') as o:
            objekt = s.read()
            objekt = ast.literal_eval(objekt)
            ID = 1
            sez = []
            for oglas in objekt:
                uredi_oglas(oglas, ID)
                sez.append(oglas)
                ID += 1
            print(sez, file=o)

def zapise_v_json(vhodna, izhodna):
    '''zapise v json datoteko s pomocjo orodij, v vhodni datoteki morajo biti podatki v slovarjih, locenih z vejico'''
    with open(vhodna, 'r', encoding='utf-8') as s:
        objekt = s.read()
        objekt = ast.literal_eval(objekt)
        orodja.zapisi_json(objekt, izhodna)


def oblikuj_model(oglas):
    '''popravi model in znamko, ker imajo nekateri avti 2 besedi v modelu oziroma znamki'''
    model, znamka = oglas['Model'], oglas['Znamka']
    model = model.split()
    if znamka == 'Alfa':
        znamka = 'Alfa Romeo'
        model = model[1]
    elif znamka == 'BMW' or znamka == 'Tesla':
        model = ' '.join(model[:2])
    else:
        try:
            model = model[0]
        except:
            model = ''
    oglas['Model'] = model
    oglas['Znamka'] = znamka

def motor(oglas):
    motor = oglas['motor'].split(',')
    #print(motor)
    with open('ocisceno.html', 'w', encoding='utf-8') as o:
        if len(motor)>1:
            oglas['prostornina motorja'] = int(motor[0].split(' ')[0])
            kw, km = motor[-1].split('/')
            kw = int(kw.strip().split(' ')[0])
            km = int(km.strip().split(' ')[0])
            oglas['moc v KW'] = kw
            oglas['moc v KM'] = km
            oglas.pop('motor', None)
        else:
            #print(motor)
            try:
                kw, km = motor[0].split('/')
                kw =  int(kw.strip().split(' ')[0])
                km = int(km.strip().split(' ')[0])
            except:
                if motor[0].strip()[-1] == 'W':
                    kw =  int(motor[0].strip().split(' ')[0])
                    km = None
                elif motor[0].strip()[-1] == 'M':
                    kw =  int(motor[0].strip().split(' ')[0])
                    kw = None
            oglas['prostornina motorja'] = None
            oglas['moc v KW'] = kw
            oglas['moc v KM'] = km
            oglas.pop('motor', None)


def uredi_oglas(oglas, ID):
    '''uredi kljuc motor in pri ceni, moci, prevozenih km in prvi registraciji string spremeni v integer'''
    oglas['ID'] = ID
    oblikuj_model(oglas)
    motor(oglas)
    cena(oglas)
    oglas['Prevozeni Km'] = int(oglas['prevozeni'])
    oglas.pop('prevozeni', None)
    oglas['Prva registracija'] = int(oglas['Prva'])
    oglas.pop('Prva', None)
    #print(oglas)
    
def cena(oglas):
    #print(oglas['cena'])
    try:
        oglas['cena'] = int(oglas['cena'])
        #print(oglas['cena'])
    except:
        oglas['cena'] = int(float(oglas['cena']) * 1000)
        #print(oglas['cena'])
        
    
    
#with ope#n('slovari.html', 'r', encoding='utf-8') as s:
#    with open('slovarji_z_vejico.html', 'w', encoding='utf-8') as v:
#        for vrstica in s:
#            print(vrstica, end=',', file=v)

funkcija1('test.html', 'ocisceno.html')
zapise_v_json('ocisceno.html', 'avti.json')
with open('ocisceno.html', 'r', encoding='utf-8') as f:
    slovarji = f.read()
    slovarji = ast.literal_eval(slovarji)
    orodja.zapisi_csv(slovarji, ['Znamka', 'Model', 'cena', 'Prevozeni Km', 'Prva registracija', 'gorivo', 'menjalnik', 'prostornina motorja', 'moc v KM', 'moc v KW', 'ID',], 'avti.csv')
