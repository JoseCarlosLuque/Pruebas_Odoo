
# Gestion de biblioteca (biblioteca_proyecto)

## ✨ Funcionalidades Destacadas

### 📖 Gestión de Libros
* **Estados Dinámicos:** Seguimiento del ciclo de vida del libro (Disponible, Prestado, Perdido).
* **Vistas Optimizadas:** Organización por categorías y autores con búsqueda avanzada.

### 👥 Gestión de Socios
* **Smart Buttons:** Acceso directo desde la ficha del socio a todos sus préstamos activos.
* **Historial Completo:** Registro detallado de cada usuario y su comportamiento de devoluciones.

### ⏳ Control de Préstamos (El Motor del Módulo)
* **Flujo de Trabajo:** Botones de validación para pasar de `Borrador` -> `En curso` -> `Devuelto`.
* **Semáforo de Retrasos:** Sistema de alertas visuales en la vista de lista:
    * 🔴 **Rojo:** Préstamos fuera de plazo.
    * 🟢 **Verde:** Préstamos activos a tiempo.
    * ⚪ **Gris:** Préstamos finalizados o borradores.
* **Automatización (Cron):** Tarea programada que revisa diariamente los plazos y marca los retrasos sin intervención humana.

---

## 🛠️ Aspectos Técnicos Implementados

Este proyecto cubre los pilares fundamentales del desarrollo en Odoo:
* **Modelado:** Relaciones `Many2one` entre libros, usuarios y préstamos.
* **Lógica Computada:** Uso de `@api.depends` para calcular si un libro está fuera de plazo en tiempo real.
* **Interfaz de Usuario (UI):** * Uso de `widgets` avanzados (`badge`, `statusbar`, `boolean_toggle`).
    * Decoraciones condicionales en vistas de lista.
* **Seguridad:** Reglas `ir.model.access.csv` para la gestión de permisos.
* **Datos de Prueba:** Archivos XML para carga masiva de libros y socios iniciales.

---

## 📁 Estructura del Proyecto

```
custom_addons/
└── biblioteca_proyecto/
    ├── __init__.py
    ├── __manifest__.py
    ├── data/
    │   ├── demo_prestamos.xml    # Datos de prueba
    │   └── ir_cron_data.xml      # Acción planificada (Cron)
    ├── models/
    │   ├── __init__.py
    │   ├── libro.py             # Definición de libros y estados
    │   ├── usuario.py           # Gestión de socios
    │   └── prestamo.py          # Lógica de préstamos y cálculos
    ├── security/
    │   └── ir.model.access.csv   # Permisos de acceso por grupos
    ├── static/
    │   └── description/
    │       └── icon.png          # Logo del módulo
    ├── views/
    │   ├── menu_view.xml         # Estructura de menús principal
    │   ├── libro_view.xml        # Vistas (lista, form) de libros
    │   ├── usuario_view.xml      # Vistas de socios y Smart Buttons
    │   └── prestamo_view.xml     # Vistas de préstamos y decoraciones
    └── README.md
```
---

## 🚀 Instalación y Configuración

1. **Requisitos:** Tener una instancia de Odoo (v16, v17 o v18) instalada.
2. **Despliegue:** - Coloca la carpeta `biblioteca_proyecto` en tu directorio de `addons`.
   - Asegúrate de que la ruta esté en el `addons_path` de tu archivo de configuración `odoo.conf`.
3. **Activación:**
   - Reinicia el servidor.
   - Ve a **Ajustes > Activar modo desarrollador**.
   - En **Aplicaciones**, haz clic en **Actualizar lista de aplicaciones**.
   - Busca "Biblioteca Proyecto" e instala.

---

## 📈 Próximos Pasos (Roadmap)
- [ ] **Chatter:** Implementar el hilo de mensajería para dejar notas en los préstamos.
- [ ] **Informes PDF:** Generación de carnets de socio y recibos de préstamo.
- [ ] **Líneas de Préstamo:** Permitir múltiples libros por cada registro de préstamo (One2many).

---


## 🤝 Contribuciones

Puedes sugerir cualquier cambio o propuesta. Todo feedback es bienvenido.
