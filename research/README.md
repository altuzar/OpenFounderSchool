# Investigación y límites de cobertura

Fecha de corte: **28 de octubre de 2026**, Ciudad de México. Esta es una investigación de materiales públicos, no acceso al currículo interno ni una auditoría de la escuela. Los precios, plazas, fechas y productos pueden cambiar.

- [Fuentes del sitio y observaciones](website-notes.md).
- [Mentores e invitados mencionados por la fuente](mentors-reference.md).
- [Notas de las 21 publicaciones de YouTube](youtube-notes.md).
- [Inventario estructurado del canal](youtube-catalog.json).
- [Inventario de páginas recuperadas](website-catalog.json).
- [Decisiones de adaptación](design-decisions.md).

## Método

Se resolvió founder.school hacia founders.school, se consultó su sitemap y se recuperaron páginas públicas enumeradas allí. Se leyó el contenido curricular público, las FAQ y materiales editoriales; el primer año también expone contenido de acordeones en la respuesta HTML, revisado para no depender sólo de texto inicialmente visible. Las vacantes se examinaron por su información de operación y alcance; no se usaron para reproducir una organización privada ni se aplicó a empleos.

Se intentaron las **29 URLs del sitemap**: veinte capturas HTTP completas terminaron correctamente; nueve agotaron el tiempo de captura. Se examinó el texto disponible en respuestas parciales o mediante el lector web, según registra el catálogo. Esto no equivale a conservar una copia íntegra verificable de cada respuesta ni a leer cada formulario y ficha de empleo palabra por palabra.

El canal público devolvió seis videos largos y quince Shorts. Se revisó **el texto completo de sus subtítulos automáticos en inglés**, con metadatos y un **muestreo de tres imágenes por publicación**. Para trece Shorts se pudieron extraer fotogramas; para los demás se usaron imágenes de storyboard de YouTube por fallos de descarga de video. No fue una reproducción audiovisual continua ni una verificación de cada palabra o pantalla. Los subtítulos pueden equivocar nombres, cantidades y marcas.

Las traducciones automáticas al español devolvieron HTTP 429; algunas descargas de video devolvieron HTTP 403. Esto no impidió leer los subtítulos ingleses de las 21 publicaciones. Se conservaron hashes de las fuentes consultadas para trazabilidad, sin redistribuir textos o medios completos. Los archivos de investigación de terceros quedaron fuera del repo público y de los paquetes.

## Qué no se afirma

No se auditó el resultado académico, ingresos, utilidad o patrimonio de alumnos, fundadores o invitados. Los números en un título, entrevista o demostración son **afirmaciones de esa fuente**, no resultados verificados. No se accedió a FounderOS, cuentas de alumnos, plataforma académica, contrato privado de inscripción o contenido tras login. No se completaron formularios ni se solicitó información en nombre de una familia.

No se verificaron exhaustivamente artículos o videos externos enlazados en prensa: son otro corpus. El inventario corresponde a la superficie pública y al momento de consulta; no prueba que no existan publicaciones privadas, retiradas o futuras. Las imágenes muestreadas permiten revisar contexto visual, no certificar toda la ejecución mostrada.

## Reproducibilidad y derechos

El catálogo registra URL, estado de recuperación, fecha y hash cuando hay bytes descargados. Un hash no demuestra que una afirmación sea cierta. Una nueva captura puede variar por contenido dinámico. Cualquier actualización debe ser manual, acotada y respetar acceso del proveedor; no se instala un scraper recurrente.

El currículo, ejercicios, lectura breve, coach y plantillas son originales de OpenFounderSchool. Las referencias no otorgan licencia sobre los materiales de Founders School. Se enlaza al original y se incluyen paráfrasis breves, sin vender acceso a sus mentores ni atribuirles participación aquí.
