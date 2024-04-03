# Player_Recommender

El objetivo final de este proyecto es encontrar a los jugadores más parecidos a aquel que sea seleccionado a través de una consulta de búsqueda, pero ¿cómo lograrlo? Cuando se trata de datos de alta dimensionalidad, la distancia euclidiana puede falsear la medida de similitud entre dos vectores. La métrica de similitud coseno puede ayudar a superar este problema.

La similitud coseno mide la similitud entre dos vectores de un espacio de producto interior. Se mide por el coseno del ángulo entre dos vectores y determina si dos vectores apuntan aproximadamente en la misma dirección. Su valor oscila entre -1 y 1, donde -1 es perfectamente disímil y 1 es perfectamente similar.

Una vez solucionado el problema de la métrica a utilizar, esta se multiplica por cien para obtener el porcentaje correspondiente.

Mención a la página web de FBref, fuente de la que se ha extraído la información para la elaboración de la base de datos: https://fbref.com/

**Instalar todos los paquetes desde un archivo requirements.txt usando pip y Python:**<br>
```pip install -r requirements.txt```

https://github.com/joaquinvictorias/Player_Recommender/assets/120015424/d4fa8f90-4bd6-4e64-acb8-b918c41324d6

