# Pi desde pi.dev

Es el harness de agentes de [pi.dev](https://pi.dev/), no otro producto llamado Pi. La [documentación de configuración](https://pi.dev/docs/latest/configuration) describe AGENTS.md y prompts locales en `.pi/prompts/`.

## Instalación por el adulto

Sigue [el inicio oficial](https://pi.dev/docs/latest/quickstart), revisa el instalador y configura un proveedor elegible con su propio presupuesto. No ejecutamos instaladores ni damos claves desde este repo. Una instalación de Pi no hace gratuitos los modelos o herramientas que utilice.

## Usar el currículo

1. Clona o descomprime el repo en una carpeta dedicada, sin documentos personales vecinos a los que el agente tenga acceso.
2. Abre tu terminal en esa carpeta e inicia Pi según su instalación (`pi`).
3. Revisa las instrucciones de proyecto que cargó: AGENTS.md pide leer COACH.md y los materiales mínimos.
4. Cuando corresponda, concede confianza al proyecto tras revisar archivos. El prompt incluido es Markdown, no una extensión ejecutable.
5. Usa `/ofs-session` si se descubrió el prompt local `.pi/prompts/ofs-session.md`; como alternativa universal pega prompts/SESSION.md y especifica la lección.
6. Ejecuta la prueba común y comienza en simulación. Autoriza únicamente la carpeta privada del alumno para entregables, manteniendo el currículo público como referencia.

## Comprobar y salir

Pide al agente enumerar los archivos que leyó y el criterio de semana 1. Guarda el checkpoint como texto o archivo autorizado. Cierra la sesión al terminar. No añadas paquetes de subagentes, automatización, MCP ni reemplaces el system prompt para cursar el programa.

Las instrucciones de archivo no son un sandbox. Configura el acceso de herramientas con el adulto y consulta las opciones de seguridad del proveedor. La adaptación no fue probada con un runtime Pi real: se verificaron rutas y paquete, no autenticación o ejecución de modelos.
