# Farmatodo Front – Automatización E2E

Automatización de pruebas end-to-end para validar el flujo de compra en la tienda de demostración de Sauce Labs (`https://www.saucedemo.com/`). El proyecto sigue el patrón Screenplay adaptado a Playwright y Pytest para mantener responsabilidades claras y pruebas fáciles de extender.

## Stack principal
- Python 3.11+
- Playwright (API síncrona)
- Pytest
- Allure Framework (reportes)

## Estructura de carpetas

```text
src/
  farmatodo/
    conf/               # Configuración del navegador y URLs
    enums/              # Enumeraciones/constantes de uso transversal
    exceptions/         # Validaciones y aserciones reutilizables
    features/           # Suites de pruebas organizadas por módulo
      login/
        test_login.py   # Flujo E2E de compra
    Interactions/       # Apertura de navegador y acciones de bajo nivel
    models/             # Page Objects / Selectores
    tasks/              # Acciones de alto nivel agrupadas por dominio
    util/               # Utilitarios y almacenamiento temporal de datos
```

## Requisitos previos
- Python 3.11 instalado y disponible en PATH.
- Navegadores de Playwright: `python -m playwright install`.
- (Opcional) Allure Commandline para reportes HTML: [Instrucciones oficiales](https://docs.qameta.io/allure/#_installing_a_commandline).
- `pip` y `venv` actualizados (`python -m pip install --upgrade pip`).

## Configuración inicial
1. Clonar el repositorio.
2. Crear y activar un entorno virtual:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Instalar dependencias (ajusta según el archivo de requisitos que gestiones en el proyecto):
   ```powershell
   pip install playwright pytest allure-pytest
   ```
   > Si mantienes un `requirements.txt`, reemplaza el comando anterior por `pip install -r requirements.txt`.
4. Descargar los navegadores soportados por Playwright:
   ```powershell
   python -m playwright install
   ```

## Ejecución de las pruebas
- Ejecutar todo el suite:
  ```powershell
  pytest
  ```
- Ejecutar únicamente el flujo de compra exitoso:
  ```powershell
  pytest -m e1_successful_purchase
  ```
- Forzar la generación de resultados para Allure (directorio configurable):
  ```powershell
  pytest --alluredir=reports/allure
  ```

Los marcadores disponibles están definidos en `pytest.ini`:
- `purchase`: agrupa los escenarios relacionados con el módulo de compras.
- `e1_successful_purchase`: caso end-to-end de compra exitosa.

## Reportes con Allure
Después de ejecutar las pruebas con `--alluredir`, genera/visualiza el reporte:
```powershell
allure serve reports/allure
```

## Personalización y configuración
- La URL base se centraliza en `src/farmatodo/conf/browser/conf_browser.py`.
- `GoLogin` abre el navegador con la configuración responsive especificada (`Desktop Chrome` por defecto). Ajusta el dispositivo según la lista de dispositivos de Playwright.
- `UtilRememberDataProcess` almacena datos temporales (nombre y precio del producto) para validaciones posteriores. Si necesitas nuevos datos compartidos, extiende esta clase o crea un utilitario similar.

## Buenas prácticas sugeridas
- Mantén los selectores en las clases de `models` para evitar duplicidad.
- Usa las `tasks` para orquestar pasos de negocio y las `exceptions` para centralizar las aserciones.
- Cuando agregues nuevos flujos, crea una carpeta dentro de `features/` y reutiliza el patrón existente (`task` + `question`).
- Documenta nuevos fixtures o hooks de Pytest en `pytest.ini` o en un módulo dedicado.

## Soporte y próximos pasos
- Añade más escenarios (por ejemplo, flujos negativos o diferentes perfiles de usuario) siguiendo la misma estructura.
- Integra la suite en un pipeline CI (GitHub Actions, GitLab CI, etc.) ejecutando `pytest` y publicando el reporte Allure.
- Considera parametrizar credenciales sensibles mediante variables de entorno o un gestor de secretos antes de llevar el proyecto a producción.

---

¡Listo! Con esto tienes la referencia principal para levantar y extender la automatización de pruebas del proyecto Farmatodo Front.