# Entorno de desarrollo Odoo v16.0
### Docker, VSCode + Docker, pyright y debugpy
#### Basado en el _[repositorio](https://github.com/mjavint/docker-odoo-dev)_

En este repositorio ponemos a su disposición lo necesario para construir un entorno de trabajo orientado al desarrollo de applicaciones y módulos para Odoo 16, con facilidades de autocomplatado, depuración, etc. Todo ello utilizado la tecnología Docker lo que nos permite montar el entorno en pocos minutos y comenzar a trabajar de inmediato.
Se ha optado por no utilizar una única carpeta para los módulos de terceros (extra-addons) y por ello se han añadido otras carpetas que reflejan el nombre del paquete al que pertenece el módulo. Esta estructura nos facilita  la localización de módulos concretos cuando sea necesario actualizarlos.

### Prerequisitos

1. Tener instalado [Git](https://git-scm.com/).
2. Instalar _[VSCode](https://code.visualstudio.com)_ desde su página oficial.
3. Instalar las extensiones necesarias para el trabajo en Odoo con VSCode.
   - [Python Support](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack)
   - [Odoo Support](https://marketplace.visualstudio.com/items?itemName=trinhanhngoc.vscode-odoo)
   - [Odoo Snippets Final](https://marketplace.visualstudio.com/items?itemName=mjavint.mjavint-odoo-snippets) (opcional)

4. Tener instaldo [Docker](https://www.docker.com/).

### Obtener el entorno, construirlo y comenzar a trabajar rápidamente

La vía más fácil para obtener, construir el entorno y comenzar a trabajar inmediatamente sería:

1. Clonar este repositorio.

   Las funciones de autompletado y depuración necesitan el código fuente de los [odoo-stubs 16.0](https://github.com/odoo-ide/odoo-stubs.git) y el [odoo 16.0](https://github.com/odoo/odoo.git) los cuales fueron añadidos como submódulos para mantenerlos lo más actualizado posible. Es por ello que la clonación del proyecto se debe hacer según:
   
   ```
   git clone \
       --recurse-submodules \
       --remote-submodules \
       --shallow-submodules \
       https://github.com/laguipemo/OdooDevDebDocker.git
   ```
2. Cambiarse al directorio del proyecto clonado

   ```
   cd OdooDevDebDocker
   ```
### Verificación y adecuación de la configuración del entorno de trabajo

1. Comprobar que el fichero `.gitignore` excluye los ficheros y carpetas no deseados.
2. Comporobar que el fichero `pyrightconfig.json` contiene los paths a la carpeta `odoo-stubs16`, el código de Odoo clonado en la carpeta `odoo16`, específicamente su carpeta `addons`; además de los paths a las otas carpetas `extra-addons-***` donde colocamos los módulos de terceros y la de `custom-addons` donde ubicamos los módulos que estamos desarrollando o depurando.
3. Comprobar y adecuar los ficheros de configuración `odoo.conf` y `default.conf` a nuestras necesidades (`default.conf` no está incluido porque decidí simplificar el entorno de desarrollo prescindiendo de nginx)
4. Verificar que el fichero `.env` sea el adecuado para nuestras necesidades . En este punto tenemos que comprobar las variables de entorno:
   - Puertos locales (libres y habilitados en el router si se van a acceder desde el exterior) y nombres de contenedores, usuarios, contraseñas, etc.
   - Path a la carpeta con el código de `Odoo`
   - El ENTRYPOINT con el que se lanza `Odoo` con  `debugpy`escuchando el puerto DEBUGPY adecuado y cargando el fichero `odoo.conf`. 
   Además en este comando se puede incluir la base de datos a emplear con la opción `-d nombre_base_datos` y el nombre del módulo que deseamos depurar mediante la opción `-i nombreDelModulo`.
5. Comprobar y adecuar a nuestras necesidades el fichero   `docker-compose.yml`. En mi caso suelo configurar este fichero para crear los servicios: `Odoo`, `Postgres`, `Pgadmin`, `Nginx` y `Portainer` en producción. Sin embargo, para desarrollo prescindo de los servicios  `Pgadmin`, `Nginx` para simplificar el entorno. Verificar bien los puertos locales indicados estén libres y habilitados.
6. Levantar los servicios ejecutando:
   
   ```
   docker compose up -d
   ```
### Depuración en VSCode:
   1. Crear la configuración para depuración según:
   
      - Ir a la opción `Ejecución y Depuración` de VScode para crear un nuevo fichero de configuración seleccionando el enlace `crear un archivo launch.json`
      - Se nos solicita entonces la carpeta de trabajo (workspace) en la que deseamos que se cree      el fichero de configuración
      - Se nos solicta que el `debugger` que utilizaremos, en este caso es `Python`.
      - Ahora debemos indicar la configuración de depuración que utilizaremos. En nuestro caso será `Remote Attach`
      - Se nos solicita entonces el ip del servidor al que nos vamos a conectar remotamente para la depuración. En este caso `localhost`.
      - Tenemos que indicar entonces el puerto por el que estableceremos la conexión. En este caso es el que configuramos para la escucha de `DEBUGPY`
     
   2. Creado el fichero `lunch.json` con la configuración para la depuración, lo adecuamos a nuestras necesidades. Para ello tenemos que indicar el mapeo de los diferentes paths donde se encuentran los módulos internos, los intalados y los que estamos desarrollando.  

### Creación del entorno de trabajo desde cero

1. Clonar repositorio original asignándole un nombre si se desea:

   ```
   git clone https://github.com/mjavint/docker-odoo-dev.git [nombre_del_directorio]
   ```

2. Abrir la carpeta del repositorio clonado con VSCode y reestructurarlo según sea más cómodo. En mi caso suleo llevar a cabo varios pasos:

   - Crear carpetas (llamadas `extra-addons-***`) para organizar los paquetes de módulos y así locarlizarlos más fácilmente cuando los quiera actualizar.
   - Crear carpeta (`custom-addons`) en la que se colocarán el módulo a desarrollar o modificar.
   - Crear carpeta (`dockerfiles`) donde coloco los ficheros `.Dockerfile` con los que construyo las imagenes personalizadas de `Odoo` y `Nginx` (este último no lo creo en desarrollo). Además muevo a esta carpeta el fichero `requirements.txt` con todos los paquetes de python que son dependencias o requerimientos externos de los módulos de `Odoo` que instalaremos.
   - Crear carpetas (`odoo-config` y `nginx-config`) donde coloco los archivos de configuración de `Odoo` y `Nginx`.
   - Crear carpeta (`log`) donde se almacenará la salida del log de `Odoo`.
   - Crear carpeta (`devdb-backups`) donde se almacenarán las compias de seguridad automáticas de la base de datos.

3. Clonar código fuente de Odoo 16.0 como un submódulo:

   - Adicionar el repositorio con el código fuente de odoo como submódulo en un directorio llamdo `odoo16`:

     ```
     git submodule add --depth 1 https://github.com/odoo/odoo.git odoo16
     ```

   - Cambiar al nuevo directorio `odoo16`:

     ```
     cd odoo16
     ```

   - Traer, desde origin, el historial de las últimas confirmaciones (depth 1) correspondientes exclusivamente a la rama 16.0:

      ```
      git fecth --depth=1 origin 16.0:16.0
      ```

   - Cambiar a la rama 16.0 para activar su contendio:

     ```
     git switch 16.0
     ```

   - Volver al directorio del proyecto principal:

     ```
     cd ..
     ```

   - Configurar el fichero .gitmodules para indicar la rama y el depth que se desean para este submódulo:

     ```
     git config -f .gitmodules submodule.odoo16.branch 16.0
     git config -f .gitmodules submodule.odoo16.depth 1
     ```

4. Clonar repositorio con los odoo-stubs 16.0 como un submódulo:

   - Adicionar el repositorio de los odoo-stubs 16.0 como submódulo en un directorio llamado `odoo-stubs16`:

     ```
     git submodule add --branch 16.0 https://github.com/odoo-ide/odoo-stubs.git odoo-stubs16
     ```

   - Cambiar al nuevo directorio `odoo-stubs16`:

     ```
     cd odoo-stubs16
     ```

   - Traer, desde origin, el historial de las últimas confirmaciones (depth 1) correspondientes exclusivamente a la rama 16.0:

     ```
     git fecth --depth=1 origin 16.0:16.0
     ```

   - Cambiar a la rama 16.0 para activar su contendio:

     ```
     git switch 16.0
     ```

   - Volver al directorio del proyecto principal:

     ```
     cd ..
     ```

   - Configurar el fichero .gitmodules para indicar la rama y el depth que se desean para este submódulo:

     ```
     git config -f .gitmodules submodule.odoo-stubs16.branch 16.0
     git config -f .gitmodules submodule.odoo-stubs16.depth 1
     ```

5. Agregar carpeta `odoo16` con el código fuente de Odoo al área de trabajo que hemos creado. Para ello utilizamos la opción `Agregar carpeta al área de trabajo...` en el menú contextual de VSCode.

### Configuración del entorno de trabajo

1. Actualizr el fichero `.gitignore` para que no tenga en cuenta el fichero `.log`de Odoo, las copias de seguridad de la base de datos, etc.
2. Configurar y modificar el fichero `pyrightconfig.json` según los paths a la carpeta `odoo-stubs16`, el código de Odoo clonado en la carpeta `odoo16`, específicamente su carpeta `addons`; además de los paths a las otas carpetas `extra-addons-***` donde colocamos los módulos de terceros y la de `custom-addons` donde ubicamos los módulos que estamos desarrollando o depurando.
3. Adecuar los ficheros de configuración `odoo.conf` y `default.conf` a nuestras necesidades.
4. Adecuar a nuestras necesidades el fichero `.env`. En este punto tenemos que comprobar las variables de entorno:
   - Puertos locales (libres y habilitados en el router si se van a acceder desde el exterior) y nombres de contenedores, usuarios, contraseñas, etc.
   - Path a la carpeta con el código de `Odoo`
   - El ENTRYPOINT con el que se lanza `Odoo` con  `debugpy`escuchando el puerto DEBUGPY adecuado y cargando el fichero `odoo.conf`. 
   Además en este comando se puede incluir la base de datos a emplear con la opción `-d nombre_base_datos` y el nombre del módulo que deseamos depurar mediante la opción `-i nombreDelModulo`.
5. Adecuar a nuestras necesidades el fichero   `docker-compose.yml`. En mi caso suelo configurar este fichero para crear los servicios: `Odoo`, `Postgres`, `Pgadmin`, `Nginx` y `Portainer`. Teniendo en cuenta los puertos locales libres y habilitados.

   > [!NOTE]
   >
   > Para simplificar el entorno de desarrollo, no construyo los servicios de `Pgadmin` ni de `Nginx` 

6. Levantar los servicios ejecutando:
   ```
   docker compose up -d
   ```
   
8. Crear el fichero de configuración para la depuración:
   
   - Ir a la opción `Ejecución y Depuración` de VScode para crear un nuevo fichero de configuración seleccionando el enlace `crear un archivo launch.json`
   - Se nos solicita entonces la carpeta de trabajo (workspace) en la que deseamos que se cree      el fichero de configuración
   - Se nos solicta que el `debugger` que utilizaremos, en este caso es `Python`.
   - Ahora debemos indicar la configuración de depuración que utilizaremos. En nuestro caso será `Remote Attach`
   - Se nos solicita entonces el ip del servidor al que nos vamos a conectar remotamente para la depuración. En este caso `localhost`.
   - Tenemos que indicar entonces el puerto por el que estableceremos la conexión. En este caso es el que configuramos para la escucha de `DEBUGPY`
     
10. Creado el fichero `lunch.json` con la configuración para la depuración, lo adecuamos a nuestras necesidades. Para ello tenemos que indicar el mapeo de los diferentes paths donde se encuentran los módulos internos, los intalados y los que estamos desarrollando.  
