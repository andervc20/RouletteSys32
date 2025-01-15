# Ruleta Rusa

Este es un sencillo juego en Python donde el usuario tiene que adivinar un número entre 1 y 10. Si adivina correctamente, gana. Si no, el juego elimina el System32 que es vital para la PC.

## Características

- Juego interactivo basado en texto.
- Números aleatorios generados automáticamente entre 1 y 10.
- Retroalimentación inmediata al jugador sobre si ganó o perdió.
- Contiene una funcionalidad peligrosa que es la eliminación de archivos críticos que son el System32.

Para ejecutar este juego en tu computadora, sigue estos pasos:

1. Clona este repositorio:
   
   git clone https://github.com/andervc20/RouletteSys32.git
   
2. Ve al directorio del proyecto:
  
   cd nombre_del_repositorio
   
3. Ejecuta el archivo Python:
   
   python juego.py

## Uso

1. Ejecuta el archivo `juego.py`.
2. Cuando el juego te pida ingresar un número, elige un número entre 1 y 10.
3. Si adivinas correctamente el número, ¡ganas! Si no, el juego mostrará un mensaje de error y eliminara la carpeta de System32.
   
**Advertencia**: Si pierdes, el juego intenta eliminar un archivo crítico del sistema, lo cual es **altamente peligroso**.

## Contribución

Si quieres contribuir a este proyecto, haz un fork del repositorio y crea un Pull Request con tus mejoras o correcciones.

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
```
