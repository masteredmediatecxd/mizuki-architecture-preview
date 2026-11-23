# Modelo de seguridad — alcance de esta muestra

## Separación de autoridad

- El proveedor de lenguaje propone; el host conserva la autoridad.
- La presencia de una herramienta en un catálogo no la habilita para toda petición.
- La política se aplica a la acción y a sus parámetros antes de ejecutar efectos.
- Un especialista auxiliar puede aportar análisis, pero la salida del modelo no concede permisos.

## Entradas observadas

Texto proveniente de páginas, archivos, OCR, resultados de herramientas o especialistas es contenido observado. No debe convertirse en una instrucción autorizada solo porque contenga órdenes o código.

El contrato incluido rechaza ciertos orígenes observados al construir una `TaskSpec`. Es una defensa acotada: por sí sola no autentica personas, no protege todos los canales y no reemplaza las comprobaciones del host.

## Errores y efectos inciertos

Un error de ejecución se devuelve al coordinador con su estado para orientar una recuperación dentro del alcance ya autorizado. Si no se sabe si un efecto ocurrió, la operación debe reconciliarse mediante observación antes de considerar otro intento. La respuesta del modelo no puede convertir un bloqueo en autorización.

## Privacidad de la publicación

Este recorte omite deliberadamente memorias, conversaciones, datos de identidad, registros, capturas, modelos, configuraciones locales, credenciales, claves, SDK y el historial Git del proyecto de trabajo. No incluye endpoints de despliegue ni una configuración operativa de la instalación.

## Límites

Este documento presenta principios de diseño y no constituye una auditoría independiente, certificación, garantía de aislamiento ni afirmación de que todas las rutas de producción satisfagan esos principios. La aplicación completa contiene componentes experimentales y pendientes que no forman parte de esta vista pública.
