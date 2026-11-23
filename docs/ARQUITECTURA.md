# Arquitectura de Mizuki

## Propósito

Mizuki integra conversación, investigación y herramientas de escritorio en una aplicación para Windows. El principio arquitectónico central es mantener separadas la interpretación de una petición y la autorización de sus efectos.

## Flujo de una tarea

1. La aplicación recibe una petición y conserva su canal de origen.
2. El coordinador representa el objetivo, restricciones, criterios observables y presupuesto de trabajo.
3. El proveedor de lenguaje genera texto o una propuesta estructurada de herramienta.
4. El host valida la propuesta y aplica las políticas locales que correspondan.
5. Un ejecutor autorizado devuelve un recibo y, cuando es posible, una observación independiente.
6. El verificador contrasta esa evidencia con el objetivo antes de que Mizuki informe el resultado.

Un texto con apariencia de comando no equivale a una invocación. Una invocación estructurada tampoco es permiso: la decisión final corresponde al host.

## Capas y responsabilidades

| Capa | Responsabilidad |
|---|---|
| Aplicación y canales | Interfaz, ciclo de vida, recepción de voz y texto |
| Coordinación | Objetivo, planificación observable, presupuesto, recuperación y cierre |
| Proveedor de lenguaje | Interpretación y propuestas; no concede permisos |
| Catálogo y ejecutores | Validación de parámetros y ejecución de capacidades conocidas |
| Autoridad local | Alcance, políticas, permisos temporales y bloqueos |
| Diario y evidencia | Correlación entre intención, ejecución y recibos |
| Verificación | Comprobación del resultado esperado con evidencia apropiada |

La instalación puede tener capacidades desactivadas o no disponibles según su configuración y dependencias. Que una capa figure en el diseño no prueba que una función específica esté operativa en un equipo.

## Contrato público incluido

`src/mizuki_public/workflow_contracts.py` muestra una parte estrecha del diseño:

- `TaskSpec` conserva objetivo, origen y restricciones.
- `InputOrigin` diferencia entradas humanas de contenido observado o derivado.
- `TaskOutcome` distingue verificación, parcialidad, bloqueo, fallo, incertidumbre y cancelación.
- Contenido de herramientas, web, OCR o subagentes no puede crear por sí solo una tarea autorizada.

Este contrato clasifica y valida datos de flujo. No verifica identidad, no decide permisos y no ejecuta acciones.

## Proveedores y funciones auxiliares

La aplicación completa dispone de adaptadores de proveedores configurables. Esta muestra no incorpora proveedores, credenciales, conexión de red ni modelos. Los especialistas locales y los módulos experimentales del proyecto no se presentan aquí como una garantía de calidad o causalidad.

## Evidencia y cierre

El resultado de una operación se contrasta con el objetivo. Un código de salida exitoso no basta necesariamente para demostrar que el efecto solicitado ocurrió. Si el efecto no se puede reconciliar, el estado debe conservar esa incertidumbre en lugar de afirmar éxito o repetir ciegamente una escritura.
