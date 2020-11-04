import orodja
import ast

def funkcija1(vhodna, izhodna):
    '''v datoteki slovarjev olepsa model, znamko in motor  '''
    with open(vhodna, 'r', encoding='utf-8') as s:
        with open(izhodna, 'w', encoding='utf-8') as o:
            objekt = s.read()
            objekt = ast.literal_eval(objekt)
            for oglas in objekt:
                oblikuj_model(oglas)
                motor(oglas)
                print(oglas, file=o, end=r',')

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
    with open('ocisceno.html', 'w', encoding='utf-8') as o:
        if len(motor)>1:
            prostornina = motor[0]
            kw, km = motor[-1].split('/')
            oglas['prostornina motorja'] = motor[0]
            oglas['moc v KW'] = kw.strip()
            oglas['moc v km'] = km.strip()
            oglas.pop('motor', None)
        else:
            print(motor)
            try:
                kw, km = motor[0].split('/')
            except:
                kw = motor[0]
                km = motor[0]
            oglas['moc v KW'] = kw.strip()
            oglas['moc v km'] = km.strip()
            oglas.pop('motor', None)

#with ope#n('slovari.html', 'r', encoding='utf-8') as s:
#    with open('slovarji_z_vejico.html', 'w', encoding='utf-8') as v:
#        for vrstica in s:
#            print(vrstica, end=',', file=v)

funkcija1('test.html', 'ocisceno.html')
zapise_v_json('ocisceno.html', 'avti.json')
