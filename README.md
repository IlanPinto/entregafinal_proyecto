# BLOG DE BASKET

REQUISITOS

-Python 3.10

-Django 2.2

REPOSITORIO Y ENTORNO VIRTUAL

-Clonar repositorio recibido en github

-Crear y activar entorno virtual


CORRER EL SERVIDOR

-Correr las migraciones con: python manage.py migrate

-Luego: python manage.py makemigrations

-Finalmente: python manage.py runserver



ACERCA DEL PROYECTO

El objetivo del proyecto es demostrar los conocimientos adquiridos en el curso de Python de Coderhouse, en particular conocimientos relacionados al desarrollo web en Django.
Para esto, se desarrollo este blog acerca de basket, cuyo principal objetivo es la interaccion con la base datos, la creacion, eliminacion y edicion de posteos y el registro y edicion de usuarios. El blog cuenta con herencia de templates html, con un template padre del cual heredan todos los templates hijos.

NAVEGANDO EL BLOG

El entrar al dominio: / (inicio) se mostrara la pagina principal. En caso de no haberse logeado, se mostrara el saludo: Hola invitado. En caso de estar logeado, mostrara el saludo: Hola + nombre de usuario (y la foto en caso que la tenga). Alli se encontraran los siguientes botones con acceso a las siguientes paginas:

-Home: permite volver al inicio del blog.

-Jugadores: muestra los jugadores que se encuentran actualmente cargados en la base de datos,  mediante vista basada en funciones.

-Entrenadores: muestra los entrenadores que se encuentran actualmente cargados en la base de datos, mediante vista basada en funciones.

-Torneos: muestra los torneos que se encuentran actualmente cargados en la base de datos, mediante vista basada en funciones.

-Crear jugadores: permite agregar nuevos jugadores a la base de datos. Debe estar logeado para realizar la operacion.

-Crear entrenadore: permite agregar nuevos entrenadores a la base de datos. Debe estar logeado para realizar la operacion.

-Crear torneos: permite agregar nuevos torneos a la base de datos. Debe estar logeado para realizar la operacion.

-Buscar jugador: permite buscar si un jugador se encuentra o no en la base de datos. La busqueda se realiza por apellido, tal como se indica en el formulario.

-Jugadores - Vistas basadas en clases: muestra los jugadores que se encuentran actualmente cargados en la base de datos. Permite tambien eliminar, ver detalle, actualizar y crear los mismos (mediante vista basada en clases), siempre y cuando uno se encuentre logeado. Se muestra esta alternativa en Jugadores para mostrar entendimiento de vistas basadas en clases y variedad de soluciones para una misma tematica.

-Registrarse: permite registrar un nuevo usuario.

-Logout: en case de haberse logeado, permite cerrar sesion (solo aparece si el usuario ya inicio sesion).

-Iniciar sesion: en case de no haberse logeado, permite iniicar sesion (solo aparece si el usuario no inicio sesion aun).

-Editar usuario: en case de haberse logeado, permite editar los datos del usuario (solo aparece si el usuario ya inicio sesion).

-Hacer publicacion: permite crear un nuevo posteo, incluyendo una imagen. La fecha es tomada automaticamente, sin necesidad de introducirla. Debe estar logeado para realizar la operacion.

-Nuevas publicaciones: permite ver todos los posteos creados. Adicionalmente, se pueden actulizar y/o eliminar los posteos, siempre y cuando el usuario sea un super usuario.

-Sobre mi: breve descripcion acerca del autor de la pagina.

Comentarios generales:

-Todas las paginas cuentas con titulo, subtitulo e imagenes.

-Las paginas jugadores, entrenadores y torneos cuentan con autor, fecha y boton "Leer mas" (no hacia sentido ponerlo en las demas). El boton "Leer mas" lleva a una pagina que dice que no hay informacion adicional. Se agrego este boton para mostrar entendimiento del agregado de botones en todos los templates y en todos los casos el boton responde (no hay botones que no tengan accion).


Para administradores:

Todos los usuarios que tengan permiso de administrador podran ingresar al dominio/admin/, donde podran encontrar todas las bases de datos (y manipularlas segun nivel de administrador).

El superusuario es:
user: ilanpinto
password: 123456789

Link al video explicativo:
https://drive.google.com/file/d/1JOZqPXnB8y7yHwDwNhv9jL7fDqaWTyYz/view?usp=share_link