# Entorno de desarrollo Odoo v16.0
### Docker, VSCode + Docker, pyright y debugpy
#### Basado en el _[repositorio](https://github.com/mjavint/docker-odoo-dev)_

### Prerequisitos

1. Tener instalado Git.
2. Instalar _[VSCode](https://code.visualstudio.com)_ desde su página oficial
3. Instalar las extensiones necesarias para el trabajo en Odoo con VSCode.
   - [Python Support](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack)
   - [Odoo Support](https://marketplace.visualstudio.com/items?itemName=trinhanhngoc.vscode-odoo)
   - [Odoo Snippets Final](https://marketplace.visualstudio.com/items?itemName=mjavint.mjavint-odoo-snippets) (opcional)

### Creación del entorno de trabajo

1. Clonar repositorio original asignándole un nombre si se desea:

   ```
   $ git clone https://github.com/mjavint/docker-odoo-dev.git [nombre_del_directorio]
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
     $ git submodule add --depth 1 https://github.com/odoo/odoo.git odoo16
     ```

   - Cambiar al nuevo directorio `odoo16`:

     ```
     $ cd odoo16
     ```

   - Traer, desde origin, el historial de las últimas confirmaciones (depth 1) correspondientes exclusivamente a la rama 16.0:

      ```
      $ git fecth --depth=1 origin 16.0:16.0
      ```

   - Cambiar a la rama 16.0 para activar su contendio:

     ```
     $ git switch 16.0
     ```

   - Volver al directorio del proyecto principal:

     ```
     $ cd ..
     ```

   - Configurar el fichero .gitmodules para indicar la rama y el depth que se desean para este submódulo:

     ```
     $ git config -f .gitmodules submodule.odoo16.branch 16.0
     $ git config -f .gitmodules submodule.odoo16.depth 1
     ```

4. Clonar repositorio con los odoo-stubs 16.0 como un submódulo:

   - Adicionar el repositorio de los odoo-stubs 16.0 como submódulo en un directorio llamado `odoo-stubs16`:

     ```
     $ git submodule add --branch 16.0 https://github.com/odoo-ide/odoo-stubs.git odoo-stubs16
     ```

5. Agregar carpeta `odoo16` con el código fuente de Odoo al área de trabajo que hemos creado. Para ello utilizamos la opción `Agregar carpeta al área de trabajo...` en el menú contextual de VSCode.

### Configuración del entorno de trabajo
   
