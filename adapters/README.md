# Elige una plataforma

No necesitas instalar las cinco. El contenido educativo es el mismo; cambian las capacidades para leer y guardar archivos. Las guías se revisaron contra documentación pública el **28 de octubre de 2026**, hora de Ciudad de México. Las interfaces, planes, términos y acceso pueden cambiar.

| Plataforma | Tipo de adaptación incluida | Qué NO hemos probado |
| --- | --- | --- |
| [Grok Bot](grok-bot.md) | Instrucciones y archivos para un bot, carga manual | Importación nativa de plantilla o cuenta conectada |
| [Claude Project](claude-project.md) | Instrucciones del proyecto y documentos de conocimiento | Límites de tu plan y persistencia de tus chats |
| [ChatGPT Work](chatgpt-work.md) | Proyecto con fuentes o carpeta local disponible | Tu cuenta, permisos, disponibilidad de modos |
| [Pi](pi.md) | AGENTS.md y prompt local de sesión | Ejecución de un modelo/proveedor real |
| [Hermes](hermes.md) | Contexto AGENTS.md desde la carpeta del repo | Runtime, conectores, modelos o gateway reales |

Los paquetes son carpetas y Markdown, **no plugins, integraciones API ni importadores oficiales**. El repositorio genera bundles verificables; no promete instalarse automáticamente en ninguna cuenta. Antes de uso con un menor, un adulto verifica elegibilidad, permisos y tratamiento de datos del proveedor.

## Prueba común de recepción

Después de cargar el material, pide:

```text
Enumera los archivos que realmente puedes leer. Resume el criterio del año 1,
semana 1. Dime qué significa la meta del millón y cuál es la devolución máxima.
Después pregunta por mi contexto de una en una. No envíes mensajes, conectes
cuentas ni crees rutinas. Si falta un archivo, dilo antes de asumir su contenido.
```

Debe reconocer tuition US$0, máximo reembolsable US$0, ausencia de garantía de ingresos y modo inicial de simulación. Revisa [pruebas de comportamiento](../tests/behavioral-evals.md). Un resultado correcto una vez no garantiza todos los comportamientos futuros.

## Portabilidad

Guarda el checkpoint fuera del historial del modelo. Al migrar, carga COACH.md, el overview, la semana actual y el checkpoint saneado. Nunca asumas que una nueva plataforma conserva permisos previos: vuelve a establecer su alcance y vigencia. Si sólo admite texto, usa `STARTER.md` del paquete y agrega la lección siguiente cuando corresponda.
