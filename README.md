## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu sistema:

- **Python 3.10+**
- **Docker y Docker Compose**
- **Node.js 16+ y npm**
- **Git**

## Pasos de Instalación

### 1. Clona el Repositorio

```bash
git clone "url"
cd expense-tracker
```

### 2. Configuración del Backend

#### 2.1 Crear un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2.2 Instalar dependencias

```bash
pip install -r requirements.txt
```

#### 2.3 Configurar las variables de entorno

Crea un archivo `.env` en el directorio raíz y define las siguientes variables:

```env

```

### 3. Configuración del Frontend

#### 3.1 Instalar dependencias

```bash
cd frontend
npm install
```

### 4. Iniciar los Servicios

#### 4.1 Backend

```bash

```

#### 4.2 Frontend

```bash

```

### 5. Opcional: Usar Docker

Si prefieres usar Docker, puedes construir y ejecutar los contenedores con el siguiente comando:

```bash
docker-compose up --build
```

### 6. Verificación

Abre tu navegador y dirígete a `http://localhost:3000` para ver la aplicación en funcionamiento.

