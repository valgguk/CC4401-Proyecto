# Proyecto de Ingeniería de Software (Grupo 2) : Marca páginas inteligente y social para tus hobbies favoritos. 🔖⭐

<span style="font-size: 0.9em; color: #888;">
Este proyecto es una plataforma web que combina funcionalidades de red social con un sistema personalizado para registrar y seguir el progreso en material audiovisual y de lectura. Los usuarios pueden gestionar su avance en mangas, animes, libros, películas y cómics, además de interactuar con otros mediante el seguimiento de perfiles, visualización de bibliotecas públicas y publicación de reseñas.
</span>

## Clonar el repositorio:
```sh
git clone https://github.com/DCC-CC4401/2025-1-CC4401-grupo-2.git
```


## Crear el entorno virtual
```sh
python -m venv env
```

## Activar el entorno virtual (pueden hacerlo desde VSCODE, luego de tener todo listo)
```sh
env\Scripts\activate
```

## Instalar las dependencias
```sh
pip install -r requirements.txt
```

## Aplicar las migraciones
```sh
python manage.py migrate
```

## Ejecutar el servidor 
```sh
python manage.py runserver
```

## Abrir el servidor
http://127.0.0.1:8000/

## Salir del entorno virtual
<control+c> cuando se esté ejecutando


## Uso git
Hacer:
```sh
git add .
git commit -m "mensaje" 
git push 
```
### Recordar:
Siempre hacer git pull para trabajar con los últimos cambios actualizando desde la rama main (git pull)

Por buenas prácticas, `db.sqlite3` está en `.gitignore` y no se sube al repositorio.  
> Si se necesita compartir datos desde db.sqlite3, utiliza fixtures (`python manage.py dumpdata` y `python manage.py loaddata`) o scripts de carga.

## 📦 Cargar datos de prueba desde JSON (fixtures)

### Paso 1: Respaldar la base de datos

Antes de cargar nuevos datos, **siempre hacer una copia del archivo `db.sqlite3`** actual para evitar pérdidas accidentales. Por ejemplo:

```bash
cp db.sqlite3 db_backup.sqlite3
```
### Paso 2 : Aplicar migraciones

Asegurar la existencia de las tablas:

```bash
python manage.py migrate
```

### Paso 3 : Cargar datos desde fixtures

Usar el comando loaddata de Django para cargar el archivo JSON con datos nuevos o modificados:
```sh
python manage.py loaddata fixtures/items.json
```
✅ Este comando agrega los datos y/o actualiza registros según la pk.
❌ No borra datos antiguos automáticamente.

⚠️ **Importante: No usar `flush`**

Nunca usar:

```sh
python manage.py flush
```
Este comando elimina **todos** los datos de la base, no solo los que se quiere recargar.  
Si por alguna razón se hace, tener un respaldo (`db_backup.sqlite3`) para restaurar.

## Cómo generar un archivo JSON (`fixture`) con nuevos datos locales

### Paso 1: Abrir la shell de Django

```bash
python manage.py shell
```

### Paso 2: Pegar este código en la shell, pulsar dos veces Enter para ejecutarlo

```python
from django.core import serializers
from categorias.models import Item

with open("fixtures/items.json", "w", encoding="utf-8") as f:
    data = serializers.serialize("json", Item.objects.all(), indent=2)
    f.write(data)
```
### 🚪 Paso 3: Salir de la shell

Una vez generado el archivo JSON, puedes salir de la shell de Django escribiendo:

```bash
exit()
```
## Nota
- Este ejemplo **solo exporta el modelo `Item`**. Si se necesita incluir más modelos (por ejemplo, `User`, `Peticion`, etc.), se debe adaptar el código para cada uno.
- Este método **no borra nada**, solo crea un archivo `.json` con los datos actuales del modelo.

