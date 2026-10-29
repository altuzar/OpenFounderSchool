# Paquetes portátiles

Descarga o copia el ZIP de tu plataforma. Descomprímelo primero; no todos los asistentes leen archivos ZIP.

- [Grok Bot](openfounderschool-grok-bot.zip)
- [Claude Project](openfounderschool-claude-project.zip)
- [ChatGPT Work](openfounderschool-chatgpt-work.zip)
- [Pi](openfounderschool-pi.zip)
- [Hermes](openfounderschool-hermes.zip)

Cada paquete incluye `SETUP.md`, un `STARTER.md` de texto combinado, currículo completo, guías, plantillas y herramientas locales. Primero carga SETUP y STARTER; añade la semana y checkpoint que correspondan. No hace falta subir todo el contenido de una vez.

`MANIFEST.json` contiene hashes SHA-256 de sus archivos. [SHA256SUMS](SHA256SUMS) contiene hashes de los ZIPs. Para regenerar: `python3 scripts/ofs.py pack`. Los paquetes se crean localmente sin red ni costos de proveedor.

Son adaptaciones manuales de contexto; no importadores oficiales, plugins ni instalaciones en cuentas. No incluyen datos de alumnos, contraseñas, libros, videos o transcripciones completas. Si el asistente no ve archivos, pega STARTER.md y la lección actual.
