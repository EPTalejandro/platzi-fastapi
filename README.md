# platzi-fastapi
api para ver una lista de peliculas, tambien eliminar,actualizar o añadir nuevas

# Pasos para usar la api  de Movies 

> el primer paso seria clonar el repositorio de github con 
`git clone https://github.com/EPTalejandro/platzi-fastapi.git`

> luego nos desplamos a la carpeta del proyecto y ya sea en un "venv" o el ambiente global instalamos los modulos que vamos a usar con 
`pip install -r requirements.txt`

> Ya con los modulos instalados creamos nuestro servidor con "Uvicorn" usando el comando 
`uvicorn main:app --reload`
luego accedemos a la direccion que este nos de

> Ya con esto tendremos el api corriendo el servidor de uvicorn si entramos a "/docs" ceremos la ducumentacion autogenerada del programa y se podran probar todos sus metodos `