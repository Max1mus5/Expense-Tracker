# PROYECT.md

## 1. Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar una aplicación fullstack de un Expense Tracker, que permitirá a los usuarios gestionar y monitorear sus gastos de manera eficiente. El proyecto se desarrollará en fases, comenzando con una versión pequeña y escalando gradualmente en complejidad y funcionalidad.

## 2. Tecnologías

### Backend:
- **Lenguaje:** Python
- **Framework:** FastAPI
- **Base de Datos:** SQLite
- **Autenticación:** Auth0
- **Task Queue:** Celery
- **ORM:** Polar
- **Contenerización:** Docker

### Frontend:
- **Librería:** React
- **Framework:** Astro (opcional, puede ser sustituido o complementado)
- **Cache:** Memcached

## 3. Requerimientos

### Funcionales:
1. **Registro e Inicio de Sesión:** Utilizando Auth0 para la autenticación.
2. **Gestión de Gastos:** CRUD (Create, Read, Update, Delete) para los gastos.
3. **Visualización de Gastos:** Mostrar gráficos y estadísticas de los gastos.
4. **Notificaciones:** Sistema de notificaciones para recordar pagos o límites alcanzados.

### No Funcionales:
1. **Seguridad:** Uso de OAuth 2.0 con Auth0 para asegurar las rutas de la API.
2. **Rendimiento:** Implementación de caching con Memcached para mejorar la velocidad de respuesta.
3. **Escalabilidad:** Docker para contenerización y facilitar la escalabilidad.
4. **Testing:** Unit testing para las APIs y componentes clave del frontend.

## 4. Fases del Proyecto

### Fase 1: Configuración del Entorno
- Configuración de Docker para el entorno de desarrollo.
- Integración de FastAPI con SQLite.
- Configuración de React y Astro en el frontend.
- Configuración de Auth0 para la autenticación.

### Fase 2: Desarrollo del Backend
- Implementación de modelos y esquemas con Polar.
- Creación de las rutas CRUD en FastAPI.
- Integración de Celery para tareas asíncronas (ej., recordatorios de pagos).
- Pruebas unitarias del backend.

### Fase 3: Desarrollo del Frontend
- Estructura base del proyecto en React.
- Integración de Astro si se decide utilizar.
- Implementación de componentes para la gestión de gastos.
- Conexión del frontend con la API de FastAPI.
- Pruebas unitarias de los componentes del frontend.

### Fase 4: Optimización y Deploy
- Optimización de la base de datos y la cache con Memcached.
- Mejoras en la UI/UX.
- Implementación de medidas de seguridad adicionales.
- Despliegue inicial utilizando Docker.
- Documentación y preparación para la fase siguiente.

### Fase 5: Escalabilidad y Nuevas Funcionalidades
- Implementación de nuevas funcionalidades según necesidades.
- Migración de SQLite a una base de datos más robusta si se requiere.
- Ajustes en la infraestructura para soportar más usuarios.

## 5. Manejo de Git

### Branches:
- `main`: Contendrá el código en producción.
- `develop`: Rama de desarrollo donde se integran nuevas funcionalidades antes de pasar a `main`.
- `bugfix/*`: Para resolver bugs específicos.
- `hotfix/*`: Parches rápidos a producción.
- `backend/*`: Para el desarrollo del backend.
- `frontend/*`: Para el desarrollo del frontend.

### Estrategia:
- Se utilizará Git Flow como estrategia de branching.
- Cada tarea se realizará en una rama separada y se fusionará con `develop` una vez completada.
- Se realizarán pull requests para revisar y aprobar el código antes de fusionarlo con `develop`.
- Se realizarán pruebas unitarias y de integración antes de fusionar con `develop`.
- Una vez que `develop` se haran pruebas finales y se fusionará con `main` para el despliegue.


## 6. Asignación de Tareas

Se utilizará **Trello** para la gestión de tareas. Las tareas se organizarán en los siguientes tableros:
- **Backlog:** Ideas y tareas por hacer.
- **In Progress:** Tareas que se están trabajando.
- **Review:** Tareas pendientes de revisión.
- **Done:** Tareas completadas.

Cada tarea se asignará con una descripción detallada, fecha límite y la persona responsable. El progreso se revisará semanalmente.

## 7. Cronograma Tentativo

### Inicio del Proyecto: 2 de septiembre de 2024
- **Fase 1: Configuración del Entorno:** 2 semanas (2/09/2024 - 15/09/2024)
- **Fase 2: Desarrollo del Backend:** 4 semanas (16/09/2024 - 13/10/2024)
- **Fase 3: Desarrollo del Frontend:** 4 semanas (14/10/2024 - 10/11/2024)
- **Fase 4: Optimización y Deploy:** 3 semanas (11/11/2024 - 1/12/2024)
- **Fase 5: Escalabilidad y Nuevas Funcionalidades:** Continuo desde diciembre de 2024

**Fecha Tentativa de Entrega Inicial:** 1 de diciembre de 2024

  ## 8. Documentación Adicional
  - **Guía de Instalación:** Instrucciones para configurar el entorno de desarrollo.
  - **Manual de Usuario:** Documentación para el usuario final.
  - **Contribución:** Guía para contribuir al proyecto.
