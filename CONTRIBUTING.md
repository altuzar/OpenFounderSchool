# Contribuir

Aceptamos mejoras al currículo original, accesibilidad, traducciones, pruebas y
adaptaciones verificadas. Usa ejemplos sintéticos y no publiques información de
menores o clientes. Contribuir contenido implica ofrecerlo bajo MIT y tener los
derechos necesarios para hacerlo.

Para modificar una semana, edita curriculum/plan.json y regenera con
`python3 scripts/render_curriculum.py`. Las cuatro guías y primeras 40 lecciones
son salidas de ese archivo. Para cambiar estructura, edita también el renderer.

Antes de enviar un cambio:

1. Conserva el propósito after school y una actividad posible con presupuesto cero.
2. Incluye objetivo, tarea, evidencia y criterio que otra persona pueda revisar.
3. Distingue datos verificados, autorreportes, inferencias y simulaciones.
4. Para cambios de proveedor, cita documentación oficial, fecha y lo que probaste.
5. Ejecuta `python3 -m unittest discover -s tests -v`, regenera paquetes y ejecuta
   `python3 scripts/ofs.py check`.

No aceptamos promesas de ingresos, mentores inventados, copias de currículo
privado, medios ajenos sin derechos ni tareas recurrentes activadas por defecto.
Una mejora de marketing no debe esconder tuition cero o el máximo reembolsable.

Usa issues para errores del material y propuestas; nunca para subir datos
privados. Para un problema de seguridad sigue SECURITY.md. La primera edición
no promete plazos de respuesta, mentoría personal ni soporte profesional.
