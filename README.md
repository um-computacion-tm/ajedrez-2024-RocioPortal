# Ajedrez
## RocioPortal
ajedrez-2024-RocioPortal created by GitHub Classroom

# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-RocioPortal/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-RocioPortal/tree/main)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/c0eb1d03cfad7ac506d1/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-RocioPortal/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/c0eb1d03cfad7ac506d1/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-RocioPortal/test_coverage)

## Descripción:

Este proyecto es un juego de ajedrez implementado en Python que utiliza programación orientada a objetos. Permite a dos jugadores enfrentarse en un tablero de texto, respetando las reglas básicas del ajedrez. Aunque no se incluyen aspectos más complejos como jaque mate o enroque. Este juego puede ser ejecutado directamente en la consola, lo que lo hace accesible y fácil de usar. 

## ¿Como se juega?

Los jugadores alternan turnos, ingresando las coordenadas de sus movimientos. El juego finaliza cuando un jugador captura todas las piezas del oponente o decide terminar ingresando "EXIT".

## Instrucciones para ejecutar el juego:
Asegúrate de tener instalado Docker en tu sistema. Puedes consultar la documentación oficial de Docker para su instalación: [Docker](https://docs.docker.com/get-docker/).

### 1. Clonar el repositorio

```
git clone https://github.com/um-computacion-tm/ajedrez-2024-RocioPortal.git
```

### 2. Entrar al directorio del proyecto

```
cd ajedrez-2024-RocioPortal
```

### 3. Construir la imagen Docker

```
docker build -t ajedrez-2024-rocioportal .
```

### 4. Correr los tests y el juego

```
docker run -i ajedrez-2024-rocioportal
```

