# OpenFounderSchool

**Tu escuela de founders después de la escuela. Abierta, gratis y en tu propio agente de IA.**

Construye algo útil, habla con clientes, aprende a vender y lleva cuentas de verdad. Para familias, alumnos y clubes after school. Español primero; puedes pedir las sesiones en inglés.

> **“Gradúate con US$1M de profit o te devolvemos el tuition. El tuition es US$0.”**
>
> Esta es nuestra garantía con humor: la devolución máxima es **US$0**. US$1M de utilidad acumulada es una meta extraordinariamente ambiciosa, **no un resultado asegurado ni una probabilidad estimada**. Las herramientas, materiales y gastos del negocio pueden costar y no se reembolsan. Consulta [la explicación completa](docs/GUARANTEE.md).

## Empieza hoy

1. Lee [START HERE](START-HERE.md) con tu madre, padre o adulto responsable.
2. Elige [Grok Bot](adapters/grok-bot.md), [Claude Project](adapters/claude-project.md), [ChatGPT Work](adapters/chatgpt-work.md), [Pi](adapters/pi.md) o [Hermes](adapters/hermes.md).
3. Usa las [instrucciones del coach](prompts/COACH.md) y el [currículo](curriculum/OVERVIEW.md). Los paquetes de [release](release/README.md) reúnen el material para cargarlo sin programar.
4. Escribe: **“Inicia OpenFounderSchool. Hazme el onboarding de una pregunta a la vez. Quiero comenzar el año 1, semana 1, en modo simulación y con presupuesto cero.”**

Para agentes con acceso a archivos, abre este repositorio como carpeta de trabajo. Lee [AGENTS.md](AGENTS.md); las guías de plataforma explican qué se carga automáticamente y qué requiere adjuntar archivos.

## Lo que hay dentro

| Material | Uso |
| --- | --- |
| [Ruta de cuatro años](curriculum/OVERVIEW.md) | 160 semanas, 6 h/semana; 960 h en total |
| [Año 1](curriculum/years/year-1.md) | 40 lecciones con ejercicios, evidencia, preguntas y criterio de avance |
| [Años 2–4](curriculum/years/year-2.md) | Un plan semanal por año para operar, crecer y preparar el relevo |
| [Manual de familias](docs/PARENTS.md) / [alumnos](docs/STUDENTS.md) | Organización, permisos y hábitos |
| [Mentores](mentors/README.md) | Ocho roles de coach IA y protocolo de mentor humano |
| [Plantillas](templates/README.md) | Entrevistas, oferta, experimentos, números, decisiones y pitch |
| [Investigación](research/README.md) | Fuentes, inventario de YouTube, notas y límites de cobertura |
| [Herramienta local](docs/CLI.md) | Preparar tu carpeta privada, consultar lecciones y calcular utilidad |
| [Del ejercicio al negocio](docs/VENTURE-PLAYBOOK.md) | Selección, pruebas, precio, capacidad y crecimiento con evidencia |

## Diseño after school

Tres sesiones de 90 minutos y una revisión de 90 minutos: **6 horas por semana**, 40 semanas por año. Ajusta el calendario alrededor de tu escuela, descanso y actividades. Puedes recorrerlo más lento. Ruta sugerida para 14–18 años; los menores de esa edad trabajan mediante un adulto y con actividades adaptadas. Antes de usar cualquier proveedor, el adulto verifica edad mínima, acceso autorizado y condiciones actuales; este repo no concede acceso a sus servicios.

No sustituye una escuela acreditada ni emite títulos oficiales. Se puede completar con papel, archivos locales y simulaciones. Las ventas reales son opcionales y requieren organización y supervisión apropiadas. La evaluación reconoce evidencia y habilidades, incluso cuando el negocio no vende.

## Costo e independencia

- Currículo y código originales: **MIT**. Puedes copiar, modificar y redistribuirlos, también comercialmente, conservando la licencia.
- Sin backend, cuenta central, telemetría, cron, newsletter obligatoria ni suscripciones del proyecto. En reposo: **0 llamadas de IA y 0 escrituras de base de datos**.
- Los proveedores de IA, hosting y cobros tienen sus propios términos y precios. No necesitas contratar todos: elige uno o trabaja offline. [Presupuesto](docs/COSTS.md).
- Proyecto independiente, inspirado por materiales públicos de [Founders School](https://founders.school/). No está afiliado a Founders School, Alpha School ni a sus mentores. No redistribuye su currículo privado, libros, videos ni transcripciones completas. [Atribución](NOTICE.md).

## Para colaboradores

Python 3.10+; sin dependencias externas ni llamadas de red en ejecución normal.

```sh
python3 scripts/ofs.py check
python3 -m unittest discover -s tests -v
python3 scripts/ofs.py pack
```

Consulta [CONTRIBUTING](CONTRIBUTING.md), [seguridad](SECURITY.md), [límites de la primera edición](docs/VALIDATION.md) y [English quickstart](README.en.md).
