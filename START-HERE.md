# Tu primera tarde

Tiempo: 45 minutos con un adulto y 45 minutos de exploración. Necesitas libreta o carpeta local; no necesitas tarjeta de crédito.

1. El alumno decide si quiere participar y qué le da curiosidad. El adulto acuerda un horario sostenible. No conviertas la meta económica en presión familiar.
2. Elige modalidad: solo con adulto, equipo de 2–3, o club de 4–8. Identifica un responsable del club y un canal privado para familias. No hay comunidad central administrada por este repo.
3. Anota únicamente alias, rango de edad, idioma, horas disponibles, intereses y presupuesto. No subas domicilio, escuela, fecha de nacimiento, documentos ni contraseñas.
4. Lee [el pacto de trabajo](docs/SAFETY.md). Empieza en simulación. La IA prepara borradores; el alumno explica y ejecuta las partes que ha entendido.
5. Sigue el adaptador de tu plataforma. Si no admite archivos, pega COACH.md y la lección actual. No pegues todo el repositorio en cada mensaje.
6. Realiza [la primera lección](curriculum/lessons/y1-w01.md). Guarda un inventario de problemas cotidianos, una hipótesis y un plan pequeño para esta semana.
7. Cierra con: qué hiciste tú, qué hizo la IA, qué aprendiste y cuál es el siguiente paso.

## Si trabajas con terminal

Desde la raíz del repositorio:

```sh
python3 scripts/ofs.py init --alias aprendiz
python3 scripts/ofs.py lesson --year 1 --week 1
```

Se crea `private/aprendiz/`, ignorado por Git. Un alias solo admite letras ASCII, números, guiones y guion bajo. Nunca uses el nombre completo del alumno como alias público. No publiques tu carpeta privada. Una regla de `.gitignore` no elimina archivos ya publicados.

## Mensaje de arranque

```text
Usa OpenFounderSchool como currículo after school. Lee las instrucciones del
coach y la lección actual. Entrevístanos de una pregunta a la vez: rol de quien
contesta, alias, rango de edad, idioma, tiempo e intereses. Pregunta si hay
adulto responsable antes de actividades externas. No recojas datos sensibles.
No me pidas crear cuentas ni conectar email para comenzar. Presupuesto US$0,
modo simulación, sin mensajes externos ni tareas programadas. Al finalizar,
dame una acción de 20 minutos y el resumen para guardar en mi carpeta privada.
```

## Cuando algo falla

- La IA no recuerda: carga el último `checkpoint.md`, no confíes en memoria implícita.
- No lee un ZIP: descomprímelo y sube los Markdown o el `STARTER.md` del paquete.
- No tiene herramientas: usa el modo conversación y copia los entregables tú.
- El proveedor no admite la edad del alumno: trabaja en papel con un adulto; no falsifiques edad ni compartas credenciales.
- El proyecto se vuelve agotador: reduce sesiones a 45 minutos o pausa. Registra dónde retomar.
