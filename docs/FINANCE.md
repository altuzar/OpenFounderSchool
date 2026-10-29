# Caja, utilidad y la meta del millón

Para empezar, el alumno debe poder explicar estas diferencias con un ejemplo propio:

| Concepto | Qué representa | ¿Cuenta como profit? |
| --- | --- | --- |
| Venta cobrada | Dinero recibido por entregar algo | Sólo después de costos y ajustes |
| Reserva o factura pendiente | Compromiso o cobro por recibir | No en el registro base caja |
| Inversión/préstamo | Financiamiento | No |
| Valuación | Estimación de valor de la empresa | No |
| Retiro del dueño | Movimiento a su cuenta personal | No es un nuevo gasto operativo |
| Utilidad | Resultado económico luego de costos | Debe especificar período y base |

## Registro educativo

`templates/ledger.csv` usa importes positivos y una categoría por fila: `revenue`, `refund`, `cogs`, `opex`, `tax`, `investment`, `loan`, `owner_draw`, `transfer`. La categoría decide el signo. No ingreses una devolución negativa: se restaría dos veces. Usa identificador único, fecha ISO, moneda, referencia anónima de evidencia y `real` o `simulation`.

`usd_per_unit` es cuántos US$ vale una unidad de la moneda de esa fila. Para USD es exactamente 1. Para MXN usa un tipo documentado por el adulto en la referencia; el programa no busca divisas ni verifica su vigencia. No mezcles importes sin conversión ni ajustes con números elegidos para alcanzar la meta.

Indicador educativo base caja USD = cobros `revenue` − `refund` − `cogs` − `opex` − `tax`. Financiamiento, retiros y transferencias se muestran aparte y no alteran ese indicador. Sólo cuenta `real` por defecto; `--simulation` calcula exclusivamente las filas simuladas.

Este indicador no resuelve inventarios, depreciación, devengos, impuestos personales ni consolidación entre negocios. Registra costos faltantes aunque descubras que el negocio pierde. Incluye trabajo pagado de terceros e IA. Lleva horas del alumno por separado y considera un costo de tiempo hipotético al evaluar si el negocio tiene sentido, sin confundirlo con un pago registrado.

## Ejemplo ficticio

Ventas US$1,000; devoluciones US$50; costos directos US$300; operación US$100; impuestos registrados US$50: indicador US$500. Una inversión de US$10,000 no lo vuelve US$10,500. Una valuación de US$1M tampoco lo cambia. Si no conoces impuestos pendientes o faltan costos, marca el resultado como provisional.

Consulta `examples/ledger-demo.csv` y ejecuta `python3 scripts/ofs.py profit examples/ledger-demo.csv --simulation`. No subas tickets o datos bancarios al repo. Conserva soporte privado y revisión adulta; antes de cualquier declaración pública de utilidad neta, reconcilia con una persona competente.
