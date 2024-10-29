from setuptools import setup
setup(
    name="paqueteprueba",
    version="1.0",
    description="Paquete de redondeo y potencias",
    author="Victor Munoz Rodas",
    author_email="ebibari1@gmail.com",
    packages=["calculos","calculos.redodeo_potencia"]
)
#comando para generar paquetes distribuibles  python setup.py sdist
#instalacion de paquete pip3 install (nombre)