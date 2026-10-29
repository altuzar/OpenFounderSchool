# Presupuesto y operación en reposo

El programa cobra US$0. Esto no vuelve gratuitas las herramientas externas. Puedes usar papel y materiales locales, o un asistente que ya tengas y cuyo uso sea elegible. No se requiere VPS, base de datos, dominio, API, anuncios ni procesador de pagos para aprender.

## Qué se ejecuta

| Modo | Con cero usuarios | Frecuencia | Despliegues | Estimación |
| --- | --- | --- | --- | --- |
| Archivos locales | Nada | Sólo al abrir o ejecutar comandos | Ninguno | 0 llamadas IA/día y /mes; 0 escrituras DB |
| Coach conversacional | Nada generado por este repo | Sólo solicitudes manuales | Un proveedor elegido por familia | Depende de mensajes y plan |
| Herramientas Python | Lectura/escritura local | Una ejecución por comando | Computadora local | Sin API ni DB; usa CPU y disco locales |
| GitHub CI | Nada por reloj | Push o PR | GitHub Actions | Minutos según cambios; sin cron |
| Rutinización opcional futura | Fuera de esta edición | Debe cuantificarse antes de habilitar | Documentar por familia | No estimado ni activado |

Los servicios de terceros podrían mantener sesiones, máquinas o suscripciones propias aunque este repo esté inactivo. Cierra tareas remotas y revisa su panel si quieres detener costos. Pausar este currículo no cancela suscripciones de proveedores.

## Estimación de uso activo — proyección

Supuesto de planificación, no medición: cuatro sesiones/semana × 12 turnos/sesión × 4.33 semanas/mes ≈ 208 turnos/mes por alumno. Si cada turno consume 4,000 tokens de entrada y 1,000 de salida serían aproximadamente 832,000 tokens de entrada y 208,000 de salida. Herramientas, contexto grande, reintentos y agentes adicionales pueden multiplicarlo. En planes por suscripción, tokens no se convierten directamente a una factura por API.

Para API: costo aproximado = entrada en millones × tarifa de entrada + salida en millones × tarifa de salida + herramientas/hosting. Consulta precios actuales directamente en el proveedor elegido. No se fijan tarifas ni límites que puedan caducar en esta guía. No uses la cifra mencionada en un video histórico como cotización vigente.

## Presupuesto familiar

Empieza con US$0 de gasto adicional; aprovecha material, biblioteca y herramientas existentes. Antes de probar algo pagado, fija límite por experimento y por mes, quién paga y cómo apagarlo. No actives recarga automática por defecto. Lleva costos de IA, almacenamiento, pagos y devoluciones en el registro, aunque sean pequeños.

No añadas tráfico ficticio con escrituras reales para que una demo se vea activa. Prefiere fixtures locales. Una escritura puede disparar lecturas en otras suscripciones: cuenta trabajo posterior, no sólo la operación inicial. Desconecta vistas y suscripciones cuando no se estén usando si más adelante construyes una app.

Consumo ya realizado de API, I/O y cómputo normalmente no se revierte borrando datos ni deshaciendo código. Almacenamiento y consumo acumulado son distintos. Cualquier devolución o reinicio depende de las políticas del proveedor y debe comprobarse con él.
