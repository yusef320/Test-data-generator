import pandas as pd
import random
import string

# Crea DEPARTAMENTO (cod_dep: varchar(5), nombre: varchar(50), telf: char(12))

code_departamento = [random.randint(11111,99999) for i in range(15)]
dep_nom = [f"Departamento {i}" for i in range (1,len(code_departamento)+1)]
dep_telf = [random.randint(900000000,999999999) for i in range(len(dep_nom))]

df_dep = pd.DataFrame(data=zip(code_departamento, dep_nom, dep_telf),
                 columns=["cod_dep", "nombre","telf"])

df_dep.to_csv("departamento.csv", sep=";",index=False)

# Crea EMPLEADO (dni: varchar(9), nombre: varchar(50), telefono: varchar(12), categoria: varchar(15), cod_dep: varchar(5))

with open("nombres.txt", "r",encoding="UTF-8") as n:
    nombre = n.read().strip().split()

with open("apellidos.txt", "r",encoding="UTF-8") as n:
    apellidos = n.read().strip().split()

categorias = ["Médico", "Enfermero", "Ingeniero", "Contable", "Limpieza", "Marketing", "Secretario",
"Atención al cliente", "Dependiente", "Gestion de stock", "Técnico", "Informatico", "Representante"]

dni, nombres, telefonos, categoria, cod_dep = [],[],[],[],[]

for i in range(1500):
    d = str(random.randint(9999999,99999999)) + random.choice(string.ascii_letters).upper()
    if d not in dni:
        dni.append(d)
        nombres.append(random.choice(nombre) + " " + random.choice(apellidos)+ " " +random.choice(apellidos))
        t = random.randint(600000000,699999999)
        while t in telefonos:
            t = random.randint(600000000,699999999)
        telefonos.append(t)
        categoria.append(random.choice(categorias))
        cod_dep.append(random.choice(code_departamento))

df_emp = pd.DataFrame(data=zip(dni, nombres, telefonos, categoria, cod_dep),
                 columns=["dni", "nombre","telefono","categoria","cod_dep"])

df_emp.to_csv("empleado.csv", sep=";", index=False)

#Creamos ALERGIAS (nombre: varchar(15), reacciones: char(100), tratamientos: varchar(100))
# y POSEEN (dni: varchar(9), nombre: varchar(15))

df_alg = pd.DataFrame({"nombre":["cacahuetes", "nueces"], "reacciones":["asfixia","asfixia"],"tratamiento":["adrenalina","adrenalina"]})
df_alg.to_csv("alergias.csv", sep=";", index=False)

data_pos = []
for i in range(150):
    dtem = random.choice(dni)
    atem =  random.choice(["cacahuetes","nueces"])
    if (dtem,atem) not in data_pos:
        data_pos.append((dtem, atem))

df_pos = pd.DataFrame(data=data_pos, columns=["dni", "nombre"])
df_pos.to_csv("poseen.csv", sep=";", index=False)


#Crea SANITARIO (dni: varchar(9), especialidad: varchar(20))

df_med = df_emp[df_emp['categoria'] == "Médico"]
dni_m = df_med["dni"].tolist()
especialidad = [random.choice(["Medico familia", "Otorrino", "Dermatologo", "Cirjuano", "Pediatra"]) for i in range(len(dni))]
df_san = pd.DataFrame(data=zip(dni_m,especialidad), columns=["dni","especialidad"])
df_enf = df_emp[df_emp['categoria'] == "Enfermero"]
dni_e = df_med["dni"].tolist()
especialidad = ["Enfermero" for i in range(len(dni))]
df_enf = pd.DataFrame(data=zip(dni_e,especialidad), columns=["dni","especialidad"])
df_san = df_san.append(df_enf, ignore_index=True)
df_san.to_csv("sanitario.csv", sep=";",index=False)

del df_med
del df_enf
del especialidad

#Crea CONSULTA (ref_servicio: varchar(9), fecha_hora: date, motivo: varchar(200), dni_sanitario: varchar(9), dni_empleado: varchar(9))

dni_san = df_san["dni"].tolist()
ref_consultas = [random.randint(100000000,999999999) for i in range(250)]
fecha_hora = [f"{random.randint(1,28)}/{random.randint(1,12)}/{random.randint(2020,2021)} "
             f"{random.randint(10,19)}:{random.randint(1,59)}" for i in range(250)]
motivo = [f'Consulta médica {random.choice(["gripe", "covid", "lesión", "malestar", "general"])}' for i in range(250)]
dni_sanitarios = [random.choice(dni_san) for i in range(250)]
dni_empleados = [random.choice(dni) for i in range(250)]

df_con = pd.DataFrame(data=zip(ref_consultas, fecha_hora, motivo, dni_sanitarios, dni_empleados),
                 columns=["ref_servicio", "fecha_hora","motivo","dni_sanitarios","dni_empleados"])

df_con.to_csv("consultas.csv", sep=";", index=False)

#Crea CHEQUEO_SALUD (ref_servicio: varchar(9), año:date, cod_dep:varchar(5))

datos_chequeo = {"ref_servicio":[],"año":[],"cod_dep":[]}

for dep in code_departamento:
    for year in [2020,2021]:
        c = random.randint(100000000,999999999)
        while c in ref_consultas:
            c = random.randint(100000000,999999999)
        datos_chequeo["ref_servicio"].append(c)
        datos_chequeo["año"].append(year)
        datos_chequeo["cod_dep"].append(dep)

df_cheq = pd.DataFrame(datos_chequeo)
df_cheq.to_csv("chequeo_salud.csv", sep=";", index=False)

#Creamos SERVICIO (ref_servicio: varchar(9))

lista_referencias = ref_consultas + datos_chequeo["ref_servicio"]
df_servicio = pd.DataFrame(data=lista_referencias, columns=["ref_servicio"])
df_servicio.to_csv("servicio.csv", sep=";", index=False)

#Creamos MATERIAL_DISPONIBLE (cod_mat: varchar(9), descripcion: varchar(80), unidades_disponibles: int(5))

df_materiales = pd.DataFrame({"cod_material":[100012,100013],
"descripcion":["Elemento genérico para prueba", "Otro elemento para pruebas"],"unidades_disponibles":[238,278]})
df_materiales.to_csv("materiales_disponibles.csv", sep=";", index=False)

#Creamos UTILIZA (ref_servicio: varchar(9), cod_mat: varchar(9), cantidad: int(5))

utiliza = {"ref_servicio": [random.choice(ref_consultas) for i in range(50)],
"cod_mat":[random.choice([100012,100013]) for i in range (50)],
"cantidad":[random.randint(1,15) for i in range(50)]}
df_utiliza = pd.DataFrame(utiliza)
df_utiliza.to_csv("utiliza.csv", sep=";", index=False)

#Creamos MEDICAMENTOS (cod_med: varchar(9), nombre: varchar(20), unidades_disponibles: int(5))

df_medic = pd.DataFrame({"cod_med":[191918765,191918824,10000283], "nombre":["Ibuprofeno", "Paracetamol", "Salbutamol"], "unidades_disponibles":[123,222,100]})
df_medic.to_csv("medicamentos.csv", sep=";", index=False)

#Creamos RECETADO (ref_servicio: varchar(9), cod_med; varchar(9), dias_tratamiento: varchar(30), dosis_diarias: varchar(30))

datarecetado = {"ref_servicio":[random.choice(ref_consultas) for i in range(100)],
                "cod_med":[random.choice([191918765,191918824,10000283]) for i in range(100)],
                "dias_tratamiento":[random.randint(1,14) for i in range(100)],
                "dosis_diarias":[random.randint(1,4) for i in range(100)]}

df_recetado = pd.DataFrame(datarecetado)
df_recetado.to_csv("recetado.csv", sep=";", index=False)

#Creamos CITA (ref_cita:varchar(9),fecha: date, hora: date, ref_servicio: varchar(9))

ref_cita = [random.randint(100000000, 999999999) for i in range(600)]
año, fecha, hora, ref_servicioo = [],[],[],[]

for year in [2020,2021]:
    df_listacheq = df_cheq[df_cheq['año'] == year]
    listaservicio=  df_listacheq["ref_servicio"].tolist()
    for i in range(300):
        año.append(year)
        i = f"{random.randint(1,28)}/{random.randint(1,12)}/{year}"
        fecha.append(i)
        hora.append(f"{i} {random.randint(10,19)}:{random.randint(1,59)}")
        ref_servicioo.append(random.choice(listaservicio))

df_cita = pd.DataFrame(data=zip(ref_cita,año,fecha,hora,ref_servicioo),
         columns=["ref_cita","año","fecha","hora","ref_servicio"])

df_cita.to_csv("cita.csv", sep=";",index=False)


#Creamos CITADO (ref_cita:varchar(9), dni: varchar(9))

dnicit, refcit = [],[]

for year in [2020,2021]:
    for departamento in code_departamento:
        servicios = df_cheq[df_cheq['cod_dep'] == departamento]
        servicios = servicios[servicios['año'] == year]
        servicios = servicios["ref_servicio"].tolist()
        dni_departamento = df_emp[df_emp["cod_dep"] == departamento]
        dni_departamento = dni_departamento["dni"].tolist()
        for serv in servicios:
            listacitas =  df_cita[df_cita['ref_servicio'] == serv]
            listacitas = listacitas["ref_cita"].tolist()
            for per in dni_departamento:
                dnicit.append(per)
                refcit.append(random.choice(listacitas))


dfcitado = pd.DataFrame(data=zip(refcit,dnicit), columns=["ref_cita","dni"])

dfcitado.to_csv("citado.csv",sep=";", index=False)

#creamos PRUEBA (ref_prueba: varchar(9), descripcion: varchar(100))

df_prueba=pd.DataFrame({"ref_prueba":[123654982],"descripcion":["Test covid"]})
df_prueba.to_csv("prueba.csv",sep=";",index=False)

#creamos ANALISIS (ref_cita:varchar(9), dni: varchar(9), ref_prueba: varchar(9), resultado:varchar(20))

f1,f2,f3,f4=[],[],[],[]
l1=list(zip(refcit, dnicit))
for i in range(200):
    c1, c2 = random.choice(l1)
    l1.remove((c1,c2))
    f1.append(c1)
    f3.append(c2)
    f2.append(123654982)
    f4.append(random.choice(["Positivo", "Negativo"]))

df_analisis = pd.DataFrame(data=zip(f1,f3,f2,f4), columns=["ref_cita","dni","ref_prueba","resultado"])
df_analisis.to_csv("analisis.csv", sep=";",index=False)

#Creamos FACULTATIVOS_EXT (nombre: varchar(25), dir: varchar(50))

df_fac=pd.DataFrame({"nombre":["Eurofins"],"Dir":["Av. de les Balears, 31, 46023 València, Valencia, España"]})
df_realizan=pd.DataFrame({"ref_prueba":[123654982],"nombre":["Eurofins"]})

#Creamos REALIZAN (ref_prueba: varchar(9), nombre: varchar(25))

df_fac.to_csv("facultativo.csv", sep=";",index=False)
df_realizan.to_csv("realizan.csv", sep=";",index=False)

##Eliminamos año de cita ya que no lo necesitamos y generamos el csv
df_cita.drop("año", axis=1, inplace=True)
df_cita.to_csv("cita.csv", sep=";",index=False)
