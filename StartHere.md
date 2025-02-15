
# Common Folders Used in Developer Projects

This document outlines commonly used folders in software projects, their purpose, and typical files stored within them.

---

## 1. `src/` (Source Code)
- **Purpose**: Contains the main application or library code.
- **Typical Files**:
  - `main.py`, `app.js`, `index.html` (entry points for the application)
  - Modules and packages (e.g., `utils.py`, `api.js`)
  - Subfolders for components, features, or models

---

## 2. `tests/` (Tests)
- **Purpose**: Contains automated tests for the application.
- **Typical Files**:
  - Unit test files (e.g., `test_main.py`, `test_app.js`)
  - Test data (e.g., `sample_data.json`)
  - Testing configuration (e.g., `pytest.ini`, `jest.config.js`)

---

## 3. `docs/` (Documentation)
- **Purpose**: Contains project documentation.
- **Typical Files**:
  - `README.md` (overview and instructions)
  - API documentation (e.g., `api.md`, `openapi.json`)
  - Developer guides (e.g., `dev_guide.md`)
  - User manuals (e.g., `user_manual.pdf`)

---

## 4. `configs/` (Configuration)
- **Purpose**: Stores configuration files for the project.
- **Typical Files**:
  - `.spec` files (e.g., `my_project.spec` for PyInstaller)
  - Environment files (e.g., `.env`, `settings.json`)
  - YAML/JSON/XML configuration files (e.g., `config.yaml`)

---

## 5. `logs/` (Logs)
- **Purpose**: Holds log files generated during development or runtime.
- **Typical Files**:
  - `app.log` (runtime logs)
  - `error.log` (error logs)
  - Archived logs (e.g., `app-2024-12-01.log`)

---

## 6. `bin/` (Binaries)
- **Purpose**: Contains executable files or scripts.
- **Typical Files**:
  - Executables (e.g., `my_app.exe`)
  - Shell scripts (e.g., `start.sh`, `deploy.sh`)
  - Command-line tools or utility scripts

---

## 7. `build/` (Build Artifacts)
- **Purpose**: Stores compiled or build output files.
- **Typical Files**:
  - Compiled binaries (e.g., `.exe`, `.dll`)
  - Bundled JavaScript files (e.g., `app.bundle.js`)
  - Static files (e.g., `styles.css`, `index.min.html`)

---

## 8. `dist/` (Distribution)
- **Purpose**: Contains packaged or distributable files.
- **Typical Files**:
  - `.zip` or `.tar.gz` files (archived packages)
  - Installers (e.g., `.exe`, `.msi`, `.deb`)
  - Docker images (e.g., `docker-compose.yml`)

---

## 9. `temp/` (Temporary Files)
- **Purpose**: Used for temporary or intermediate files.
- **Typical Files**:
  - Cache files (e.g., `.cache`, `tmp_data.json`)
  - Temporary build artifacts (e.g., `temp.html`)
  - Debug files

---

## 10. `archive/` (Archived Files)
- **Purpose**: Stores old or unused files for future reference.
- **Typical Files**:
  - Archived builds (e.g., `my_app_v1.0.zip`)
  - Deprecated code (e.g., `old_feature/`)
  - Backup files (e.g., `config_backup_2024-12-14.yaml`)

---

## 11. `assets/` (Assets)
- **Purpose**: Contains media and other static assets used in the project.
- **Typical Files**:
  - Images (e.g., `logo.png`, `banner.jpg`)
  - Fonts (e.g., `Roboto.ttf`)
  - Audio or video files (e.g., `intro.mp3`)

---

## 12. `data/` (Data)
- **Purpose**: Stores datasets and related files.
- **Typical Files**:
  - CSV/JSON files (e.g., `users.csv`, `settings.json`)
  - Database files (e.g., `data.sqlite`)
  - Mock data (e.g., `mock_data.json`)

---

## 13. `lib/` (Libraries)
- **Purpose**: Contains external libraries or dependencies not managed by a package manager.
- **Typical Files**:
  - Custom libraries (e.g., `custom_math.py`)
  - Vendor-specific files (e.g., `vendor_library.js`)

---

## 14. `scripts/` (Automation Scripts)
- **Purpose**: Stores scripts for automating tasks.
- **Typical Files**:
  - Build scripts (e.g., `build.sh`)
  - Deployment scripts (e.g., `deploy.py`)
  - Data processing scripts (e.g., `process_data.py`)

---

## 15. `env/` (Virtual Environment)
- **Purpose**: Contains the virtual environment for Python projects.
- **Typical Files**:
  - Python executables
  - Installed dependencies (e.g., `site-packages/`)

---

## Additional Suggestions
- Use a **`.gitignore`** to exclude unnecessary files or directories (e.g., `logs/`, `temp/`, `env/`) from version control.
- Customize folders based on project requirements. For example, add a `plugins/` folder for plugin-based architectures or an `examples/` folder for code samples.

This modular structure keeps projects organized, maintainable, and scalable.
