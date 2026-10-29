# Herramienta local (opcional)

Requiere Python 3.10+ y biblioteca estándar. Los comandos no usan red, modelos, API, base de datos ni tareas en segundo plano. Ejecútalos desde la raíz del repo. Si no tienes Python, usa los Markdown y plantillas manualmente.

```sh
python3 scripts/ofs.py init --alias aprendiz
python3 scripts/ofs.py lesson --year 1 --week 1
python3 scripts/ofs.py complete --alias aprendiz --year 1 --week 1
python3 scripts/ofs.py profit private/aprendiz/ledger.csv
python3 scripts/ofs.py profit examples/ledger-demo.csv --simulation
python3 scripts/ofs.py profit examples/ledger-demo.csv --simulation --share 0.5
python3 scripts/ofs.py pack
python3 scripts/ofs.py check
```

`init` crea una carpeta privada nueva y rechaza sobrescribirla. `complete` registra avance **auto-reportado**, sin asignar una nota o certificar ventas. Repetir la misma semana no la duplica. La siguiente lección la elige el alumno/coach según la revisión; el comando no la avanza automáticamente.

`profit` valida IDs únicos, categorías, fechas, moneda y conversión. Usa importes positivos; la categoría define qué se resta. Por defecto calcula sólo filas `real`. `--simulation` calcula sólo simulaciones; jamás mezcla ambas. `--share` multiplica el indicador por la participación declarada (0 a 1, sin incluir cero), que debe respaldarse fuera del programa. No demuestra propiedad legal.

El CSV se puede editar con un editor de texto o herramienta propia. Si una hoja de cálculo altera fechas, separadores o números, conserva exactamente el encabezado y decimales con punto antes de calcular. Errores de validación detienen el cálculo: no se omiten silenciosamente filas inválidas.

`pack` escribe cinco ZIPs y SHA256SUMS en release/. Usa una lista explícita de contenidos; no incluye private/, credenciales, videos ni fuentes completas. `check` comprueba la estructura, enlaces internos y hashes de paquetes existentes. No comprueba acceso remoto a enlaces ni el comportamiento de un LLM.

Después de editar curriculum/plan.json regenera guías con `python3 scripts/render_curriculum.py`, ejecuta tests y empaqueta. No edites sólo el archivo generado si quieres conservar el cambio.
