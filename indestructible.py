import csv
import datetime
from prefect import task, Flow, Parameter
from prefect.schedules import IntervalSchedule

#La tarea se ejecuta 5 veces cada 5 seg en caso de fallar
@task(max_retries=5, retry_delay=datetime.timedelta(seconds=5))
def extract(path):
    #Se abre el archivo en modo lectura
    with open(path, "r") as f:
        text = f.readline().strip()
    data = [int(i) for i in text.split(",")]    #Se separan los datos con ,
    return data                                 #Devuelve los datos del archivo

@task
def transform(data):
    #Suma 1 a cada valor de tdata
    tdata = [i + 1 for i in data]
    return tdata            #Devuelve los nuevos valores de tdata

@task
def load(data, path):
    #Se abre el archivo en modo escritura
    with open(path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)   #Se escriben los datos en el archivo
    return

def build_flow(schedule=None):
    #Flow dentro de funcion
    with Flow("my_elt", schedule=schedule) as flow:
        path = Parameter(name="path", required=True)
        data = extract(path)
        tdata = transform(data)
        load(tdata, path)

    return flow


#Se crea un schedule para que se ejecute cada 5 segundos
schedule = IntervalSchedule(
    start_date=datetime.datetime.now() + datetime.timedelta(seconds=1),
    interval=datetime.timedelta(seconds=5)
)

flow = build_flow(schedule)
flow.run(parameters={   #Se pasa como parametro el nombre del archivo
    "path": "values.csv"
})