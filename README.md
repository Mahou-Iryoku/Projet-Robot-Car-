# Projet-Robot-Car-

_A l’occasion de ce projet, j’ai continué ce projet que j’ai effectué l’année dernière pour améliorer les différentes fonctionnalités du robot._
En effet, l’objectif est de piloter le robot sans besoin d’interaction humaine grâce à un capteur d’ultrason et d’utiliser une caméra pour effectuer de la reconnaissance d’objet. Ce robot va permet de détecter les différents objets s’il est réellement dangereux pour intervenir dans la surveillance ou dans la sécurité routière par exemple.

_Le robot est composé finalement :_

_4 moteurs à courant continu fixé à 4 roues_

_4 modules à relais sur 5V_

_Deux plaques pour fixer les composants électroniques_

_Un Raspberry Pi 4 modèle B_

_Une batterie 5V/4A + une pile d’alimentation_  

_Un régulateur de tension contenant à un condensateur de découplage et d’un interrupteur électronique._

_Un module d’une caméra du type NOIR v2_

_Un Micro SD_ 

_Un capteur d’ultrason du type HC-SR04_

__Dans notre Raspberry Pi, j’ai utilisé dans une machine Linux (système d’exploitation Raspbian)  qui va connecter à distance en réseau local l’environnement du bureau grâce au logiciel VNC Server.__ 

__Nous avons décidé d’enlever l’interface graphique et de remplacer par un nouveau script en Python pour rendre très autonome le robot. Plus précisément, le robot va automatiquement détecter les différents obstacles qui se trouve à la face avant du robot et d’identifier les objets en utilisant de la reconnaissance d’objet.
Pour que le robot soit autonome, il faudrait que le robot soit capable d’exécuter en boucle infini à plusieurs temps d’arrêt pour qui arrive à se retrouver sa vraie position du robot. Une fois qui retrouve sa position, le robot doit être capable de chercher le chemin où il souhaite d’aller.__ 
