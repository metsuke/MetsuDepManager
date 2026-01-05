# MetsuDepManager 🟡②

****** OJO PROYECTO WIP DOCUMENTACION NO FUNCIONAL TODAVIA *****

**Gestor de dependencias ético, seguro, accesible y listo para producción para Python**

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/downloads/)

## Descripción

MetsuDepManager es un gestor de dependencias para Python que actúa como un **wrapper ligero e inteligente sobre Poetry**, incorporando un motor de políticas avanzado para garantizar el cumplimiento normativo en materia de vulnerabilidades, licencias y orígenes geográficos de los paquetes.

Diseñado especialmente para entornos regulados (banca, defensa, sanidad, administraciones públicas, educación) y sistemas críticos (air-gapped, RGPD, NIS2, ENS Alto, DORA, ITAR/EAR), prioriza:

- **Ética**: sin telemetría no consentida.
- **Seguridad**: integración con bases de vulnerabilidades.
- **Accesibilidad universal**: CLI 100% compatible con lectores de pantalla (WCAG AA/AAA).
- **Privacidad y soberanía**: modo offline-first y perfiles geopolíticos.
- **Transparencia**: generación de SBOM enriquecidos (CycloneDX/SPDX).

Forma parte del ecosistema **MetsuOS**, cuya misión es promover la plena inclusión a través de los videojuegos y la tecnología accesible.

## Características principales

- Wrapper sobre Poetry con comandos proxy y adicionales éticos.
- Motor de políticas multi-capa (vulnerabilidades, licencias, origen geográfico).
- Generación y verificación de SBOM con metadatos personalizados (geoOrigin).
- CLI profesional y accesible basada en Typer + Rich (i18n: es/ca/en).
- Resiliencia geopolítica con perfiles predefinidos (EU-sovereign, defense-es, airgap...).
- Modo sandbox y soporte para entornos aislados.
- Sistema de plugins extensible.
- Sin tracking ni telemetría.

## Instalación

El proyecto está en fase de desarrollo activo (roadmap Q1 2025 - Q1 2026). Cuando esté publicado:

```bash
pip install metsudepmanager
```

O mediante binarios standalone (PyInstaller/Nuitka) para entornos air-gapped.

## Uso rápido

```bash
# Inicializar proyecto (proxy de Poetry)
metsudep init

# Añadir dependencia con políticas éticas
metsudep add requests --geo-prefer=EU

# Instalar con verificación completa
metsudep install

# Generar SBOM enriquecido
metsudep sbom generate --format=cyclonedx --include-geo

# Auditar políticas
metsudep audit
```

Configuración en `metsudep.toml` o `pyproject.toml`:

```toml
[tool.metsudep]
geo_profile = "eu-sovereign-strict"
license_profile = "eu-compliant"
```

## Tecnologías

- Python 3.11+
- Poetry (backend)
- Typer + Rich (CLI)
- Safety, OSV (vulnerabilidades)
- SQLite (caché local)
- CycloneDX / SPDX (SBOM)

## Contribuciones

¡Bienvenidas! El proyecto es 100% open-source bajo GPL-3.0.

**Importante**: Cualquier contribución que degrade la accesibilidad será rechazada automáticamente. Consulta la guía de contribuciones (próximamente) para más detalles.

## Licencia

Este proyecto está licenciado bajo la **GNU General Public License v3.0** - ver el archivo [LICENSE](LICENSE) para detalles.

## Más información

- Visión general detallada del proyecto: [metsuke.com/publicbrain/metsudepmanager](https://www.metsuke.com/publicbrain/metsudepmanager---vision-general-del-proyecto-%F0%9F%9F%A1%E2%91%A2.html)
- Documentación completa (en desarrollo con MkDocs accesible).

¡Gracias por tu interés en un software más ético y accesible!
```