# Frutos secos 2027

Informe interactivo de tendencias 2027 en snacks de frutos secos y en el consumidor (estilo de vida, bienestar y alimentación), con foco en Colombia. Corte de la investigación: 28 de octubre de 2026.

**Ver el informe:** https://nicolascarvajalnavia-cmd.github.io/frutos-secos-2027/

## Cómo está hecho

- `datos.py`: todo el contenido (tendencias, cifras, fuentes y nivel de evidencia de cada dato).
- `plantilla.html`: diseño, estilos y JavaScript (filtros, enlaces entre tendencias, tooltips de las gráficas).
- `build.py`: genera `index.html` (HTML estático; se lee completo aunque falle JavaScript).

Para regenerar: `python3 build.py`.

Investigación y consenso: Claude (Anthropic) y Codex (OpenAI). Las cifras pertenecen a sus autores; las implicaciones de negocio son lectura propia.
