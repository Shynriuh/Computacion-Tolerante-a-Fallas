# PROYECTO FINAL CatURL

# Descripción
En este repositorio se encuentra el proyecto final generado en la materia de Computación Tolerante a Fallas sección D06 por el profesor Michel Emanuel Lopez Franco.

# Integrantes del proyecto:

    Karen Lizette Flores Muñoz
    Dana Ochoa Velasco
    Luis Uriel Robles Estrada

Tecnologias utilizadas:

    React.js
    Node.js
    Docker
    Kubernetes
    Istio

Tutorial para desplegar el proyecto:

    Clonar el repositorio

Docker

    Elaborar los Dockerfile para cada microservicio
    Subirlos a DockerHub
    Crear un docker-compose.yaml
    Usar el comando docker-compose up
    Una vez en probada su funcion, se detiene con el comando docker-compose down

Kubernetes

    Comando minikube start
    Comando kompose convert
    Comando kubectl apply -f .\yaml
    Comando kubectl port-forward svc/webmvc 3000:3000
    Comando minikube dashboard

Istio

    Comando para los .yaml kubectl apply -f .\.yaml
    Comando para inyectar kubectl label namespace default istio-injection=enabled
    Comando para el monitoreo de la aplicación kubectl get svc -n istio-system
    
# CAPTURAS DEL PROYECTO

![imagen](https://user-images.githubusercontent.com/98301135/170889589-bb48a4bf-f083-452e-a635-4426b27befa3.png)

![imagen](https://user-images.githubusercontent.com/98301135/170889600-38b84e40-8750-4f2a-8244-5ca9dc8819e7.png)

![imagen](https://user-images.githubusercontent.com/98301135/170889603-44721fc7-d024-464d-aea1-f3e10dbdd600.png)


