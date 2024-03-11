# EXAMEN SXE

## Hacer que se vea la base de datos en el IDE

<img width="311" alt="1" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/a7e4a901-cc96-4a94-a73f-693ef440f1b5">

Arriba a la derecha de nuestro Pycharm cmbiamos a vista bases de datos

<img width="424" alt="2" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/fde5d7a3-6b83-4f19-a1f3-456f40c01b79">

 Y elegimos nuestra base de datos Postgress

<img width="602" alt="3" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/7952a141-448e-45fc-a3bc-fb676c502a45">

Ahora descargaremos el driver si es necesario y agregaremos nuetsras variables de acceso a la base de datos para probar si funciona

<img width="881" alt="4" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/13420567-7095-492d-9669-2f644c407446">

Con este comando vemos los nombres de los cantenedors que tenemos corriendo ahor amismo 

<img width="635" alt="5" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/229c5c8b-b280-45a9-8cef-2b9ce5517150">

Y entramos en la consola de nuestro contenedor de *ODOO*

<img width="268" alt="6" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/223230e0-6904-40b5-885a-949007340bd0">

Una vez estamos dentro tenemos que crear nuestro modulo

<img width="374" alt="7" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/fb62a0fd-915b-4816-a76a-49212eb09cee">

En este caso lo llamaremso *ExamenSXE*

<img width="365" alt="8" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/d0a0e36a-83c3-4dc0-b022-a0908570843c">

Ahora le damos permisos para poder modificar los archivos de nuestro modulo


<img width="401" alt="9" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/e1e80ee2-0d56-445b-9bbe-c8a11781e37e">

Lo primero seria ir a nuestro archivo *__manifest.py__*

<img width="379" alt="10" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/f0ca0bb0-3592-42d7-bd30-e1c8fdc343ec">

Dentro de este archivo podemos cambiarle el nombre al modulo, cmabiar la version , y añadir una descripcion breve para que salga en la interfaz de instalación

## Creacion de la tabla

<img width="413" alt="11" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/cc7acb17-ac1b-4fa0-b6b4-7e03a3bb0366">

Para crear la tabla nos vamos a nuestro archivo *models.py*

<img width="329" alt="12" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/01cb374e-5f8b-413d-95da-b538a809ac22">

Aqui creamos nuestra tabla con los tres campos necesarios

<img width="373" alt="13" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/e85432e3-3268-434b-991a-10f7f539d028">

Aqui en el mismo archivo models creamos un boton que cuando se presione agregue 5 productos a nuestar tabla

## Configuración del archivo view

<img width="409" alt="14" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/0d926e53-214e-4c8c-b462-5acb8944c9c7">

Ahora nos  vamos a nuestro archivo view


<img width="402" alt="15" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/d53fe15a-29a5-4c52-9757-9932805d884e">

Aqui descomentamos las lineas y cambiamos el apartado <field name="model"> por el nombre de nuestra tabla

<img width="443" alt="16" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/b1d5b562-6e60-41db-ae24-91d75c97c6ca">

Aqui descomentamos las lineas y en el apartado *tree* ponemos los nombres de nuestros campos

<img width="506" alt="17" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/a83e01cf-9f0b-4e0b-a508-9b535de1bd81">

Aqui unicamente descomentamos la lineas

<img width="713" alt="18" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/da6b76fd-a616-42f3-a18e-aa30c11a8472">

Aqui creamos la interfaz para que nuestro boton que crea productos aparezca en pantalla

## Configuracion de security

<img width="406" alt="19" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/81fed06b-b22a-46a8-a376-e3302787d20a">



<img width="567" alt="20" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/bd5d814c-88f1-4537-acb3-9fff3bbb6c35">

Para poder ver nuestra vista tenemos que cambiar el acceso a la vista, para ello nos dirigimos a la carpeta security y modificamos el archivo ir.model.access.csv 

## Inciar Odoo con el modulo

<img width="271" alt="21" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/852f42e1-532a-422b-bf43-d587e8572212">


Lo primero en nuestro archivo *__manifest.py__* tenemso que descomentar estas lineas para que simpre se que quede cargado

<img width="469" alt="22" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/51de5551-f6ca-4d1b-9475-30c0198e4700">

Ahora reiniciamos nuestros contenedores para que la configuracion se guarde


## Instalar modulo

<img width="467" alt="odoo" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/1c645da0-4a37-499f-9f7e-f88b4ad02338">

Creamos la base de datos 

<img width="334" alt="odoo2" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/5f6866b6-cf2e-4fb6-b381-7af4e10acb43">

Nos logueamos con nuestros credenciales

<img width="949" alt="odoo3" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/7547d51f-f236-4ec0-b3dc-94033cefd509">

y ahor auna vez ya dentro de Odoo desde el apartado de buscar aplicaciones buscamos el nombre de nuestro modulo en este caso ExamenSXE

<img width="586" alt="odoo4" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/ccd115cc-7e1b-4a52-96cf-7a6d2befd68d">

Ya dentro de nuestro modulo podemos ver los campos de la tabla , si le damos a crear nuevo campo podemos crear y editar los campos tambien podemos crear 5 productos

<img width="211" alt="odoo5" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/6aa86eb0-3efd-47fd-ae57-fbbad9996991">



<img width="1227" alt="odoo6" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/1718daa3-c0f9-4d73-9b25-4abb73a66d80">

##Ver la base de datos en el IDE

<img width="317" alt="db1" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/f24defc5-b191-451e-84b4-628e5d867684">
<img width="230" alt="db3" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/b66a6953-f08d-4faf-b169-83788c708df9">


<img width="527" alt="db2" src="https://github.com/FranciscoFerreiraT/examen_sxe/assets/92456485/ba657e52-b4df-49bf-805f-8631cd1d1922">


