# Estado y alcance de la vista pública

**Preparada:** 23 de noviembre de 2026  
**Tipo:** muestra técnica seleccionada para revisión

## Incluido

- Documentación introductoria de arquitectura y límites.
- Contrato de tareas autocontenido extraído de la base de código de Mizuki.
- Descripción del modelo de seguridad a nivel de responsabilidad.

## Excluido

- Aplicación completa, interfaz, avatar y canales de mensajería.
- Configuración personal, memorias, conversaciones y datos locales.
- Historial Git, registros, capturas, bases de datos y artefactos de ejecución.
- Credenciales, claves, archivos de entorno, pesos de modelos y SDK.
- Código de herramientas con efectos externos y subsistemas experimentales.

## Cómo interpretar el estado

Este repositorio no es instalable ni suficiente para ejecutar Mizuki. El módulo incluido sirve para inspeccionar el contrato de datos; no implementa un agente autónomo ni un sistema de permisos. La disponibilidad y el comportamiento de capacidades del producto completo dependen del código, las dependencias y la configuración de cada instalación.

La muestra no afirma ausencia de errores ni certifica que todos los controles del producto estén completos. Cualquier evaluación debe limitar sus conclusiones a los archivos presentes y a la evidencia que el evaluador haya obtenido.

## Procedencia

`src/mizuki_public/workflow_contracts.py` es una copia del módulo `Reasoning/workflow_contracts.py` del proyecto Mizuki, preparada para inspección aislada. Se conserva el contenido del contrato de origen; su inclusión no significa que el resto del sistema esté contenido o representado íntegramente aquí.
