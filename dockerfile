# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /filemanager

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt /filemanager/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al contenedor
COPY . /filemanager/

# Puerto en el que se ejecuta la aplicación Django
EXPOSE 8000
RUN apt-get update && apt-get install -y libpq-dev

#RUN python manage.py migrate
# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
