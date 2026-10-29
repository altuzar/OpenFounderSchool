# Alcance de validación — edición 0.1.0

Fecha: 28 de octubre de 2026 (Ciudad de México). Es una primera edición de material educativo original, no un programa acreditado, pilotado o evaluado por resultados de negocio.

## Comprobado localmente

- 160 semanas únicas y consultables; 40 lecciones completas del primer año; cuatro guías anuales y campos de actividad, prueba, entrega y criterio.
- Trece pruebas Python: números, separación real/simulación, devoluciones, costos, financiamiento, moneda, participación, errores, duplicados, pérdidas, alias, archivos privados y lecturas sin red.
- Ejecución de onboarding local y registro de progreso. Repetir una marca de avance no la duplica y `init` rechaza sobrescribir una carpeta existente.
- El ejemplo financiero produce US$500 en SIMULACIÓN, excluyendo US$10,000 de inversión del indicador. No certifica utilidad neta contable.
- Cinco paquetes portátiles con manifiestos y hashes. La comprobación incluye rutas, correspondencia con archivos fuente y enlaces locales en repo y dentro de los ZIPs.
- Se regeneraron los cinco ZIPs con sockets bloqueados y sus hashes coincidieron entre ambas ejecuciones. Cada paquete contiene 109 archivos, incluido el manifiesto; se usa ZIP sin compresión para evitar variaciones por versiones de zlib.
- Empaque mediante lista explícita, sin archivos privados, secretos, transcripciones ni videos. Los ejemplos incluidos son ficticios.

## Reposo y uso activo

Inspección del código: sin clientes de red, servidor, cron, loops programados, base de datos o suscripciones. La prueba activa de lectura/finanzas se ejecutó con creación de sockets bloqueada y pasó. Los comandos terminan y no dejan un servicio propio corriendo. No existe una frontera de recurrencia que esperar en este diseño.

La proyección estructural en reposo es 0 llamadas de IA y 0 escrituras DB del proyecto; no es una medición de facturación de proveedores conectados, pues no se conectó ninguno. La estimación de tokens de docs/COSTS.md es una proyección distinta, no consumo observado.

## No comprobado

No se instalaron Pi o Hermes, se importaron bots nativos ni se abrieron cuentas o Projects reales para las cinco plataformas. Sus guías se basan en documentación pública y carga manual. No se ejecutaron las evaluaciones de comportamiento contra modelos reales; cada familia debe realizar la prueba de recepción con datos ficticios antes de usar herramientas.

No hay piloto con menores, auditoría de seguridad, revisión profesional de obligaciones por jurisdicción, validación de accesibilidad con usuarios ni resultados de graduación. Las instrucciones del coach no constituyen controles técnicos de permiso. Las afirmaciones de terceros se conservan como referencias, sin certificación.

## Investigación

Se intentaron 29 páginas del sitemap; hubo capturas HTTP incompletas y se usó también texto público accesible mediante lector web. Se revisaron subtítulos ingleses completos de las 21 publicaciones públicas encontradas y tres imágenes por publicación. No se afirma visionado audiovisual continuo ni acceso al currículo privado. Consulta research/README.md y sus catálogos para el método y las limitaciones.
