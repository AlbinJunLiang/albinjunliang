Aprender Git para el mundo real va mucho más allá de hacer `git add`, `commit` y `push`. En un entorno profesional, Git es una herramienta de colaboración, auditoría y control de riesgos.

Aquí tienes una guía estructurada y práctica con los comandos esenciales, las técnicas avanzadas del día a día y los patrones de trabajo que utilizan los equipos de desarrollo profesionales.

---

## 1. Los Fundamentos que Debes Dominar (Más allá de lo básico)

Antes de pasar a flujos complejos, asegúrate de dominar estos comandos y conceptos que usaras diariamente:

* **Ver el estado y los cambios con precisión:**
```bash
git status -s               # Estado resumido
git diff                    # Cambios no guardados en el staging area
git diff --staged           # Cambios listos para el commit

```


* **Guardar trabajo temporalmente (`git stash`):**
Cuando estás en medio de una tarea y necesitas cambiar de rama urgentemente sin hacer commit:
```bash
git stash push -m "Trabajo en progreso del módulo X"
git stash list              # Ver la lista de stashes
git stash pop               # Recuperar el último stash y borrarlo de la pila

```


* **Inspeccionar la historia de forma limpia:**
```bash
git log --oneline --graph --all --decorate  # El gráfico de ramas definitivo en la terminal

```



---

## 2. El Día a Día en una Empresa: Git Avanzado

En el mundo real cometerás errores o necesitarás mantener un historial limpio y legible para tus compañeros en las Pull Requests (PR). Estos son los comandos clave:

### A. Limpiar tu historia antes de una Pull Request (`git rebase -i`)

Si hiciste muchos commits desordenados (*"fix typo"*, *"otro arreglo"*, *"ahora sí funciona"*), puedes unirlos (squash) en un solo commit limpio antes de enviarlo a revisión:

```bash
git rebase -i HEAD~4   # Abre un editor interactivo para los últimos 4 commits

```

*En el editor podrás cambiar `pick` por `squash` (s) para fusionar commits y reescribir mensajes claros.*

### B. Corregir el último commit sin cambiar el mensaje o añadiendo archivos olvidados

```bash
git add .
git commit --amend --no-edit   # Añade los cambios al commit anterior manteniendo el mensaje

```

### C. La red de seguridad absoluta: `git reflog`

¿Te equivocaste con un `reset --hard`, borraste una rama por error o hiciste un rebase desastroso? **`reflog` registra cada movimiento de la cabeza (HEAD) de Git**.

```bash
git reflog                  # Muestra una lista de cada acción reciente con un hash (ej: HEAD@{5})
git reset --hard HEAD@{2}   # Vuelve exactamente al estado en el que estabas antes del error

```

### D. Resolver conflictos como un profesional

Cuando dos personas modifican la misma línea de código, Git pausará el merge y marcará el conflicto así:

```text
<<<<<<< HEAD
tu código actual en tu rama
=======
código que viene de la otra rama (ej. main)
>>>>>>> branch-name

```

1. Abre el archivo en tu editor (VS Code te da botones directos para aceptar "Current Change", "Incoming Change" o "Both").
2. Edita, guarda y luego ejecuta:
```bash
git add <archivo-arreglado>
git rebase --continue    # o git merge --continue según el proceso que estabas haciendo

```



---

## 3. Patrones y Flujos de Trabajo (Branching Strategies)

En las empresas no se trabaja sobre `main` directamente. Se siguen flujos estandarizados:

### A. GitHub Flow (El más común en empresas de producto y startups)

Es un flujo ágil, basado en ramas de características (*feature branches*) y despliegues continuos.

1. **La rama principal (`main`)** siempre está lista para producción y es estable.
2. Para cualquier nueva funcionalidad o bug, creas una rama descriptiva desde `main`:
```bash
git checkout -b feature/autenticacion-oauth

```


3. Haces tus commits de forma atómica (un commit por cada unidad lógica de cambio).
4. Subes tu rama al repositorio remoto:
```bash
git push origin feature/autenticacion-oauth

```


5. Abres una **Pull Request (PR)** hacia `main`. Aquí ocurre la revisión de código (*code review*) con tus compañeros.
6. Una vez aprobada y pasado el CI/CD (tests automáticos), se hace el merge a `main` y se borra la rama remota.

### B. GitFlow (Común en empresas grandes o corporativas con versiones estáticas)

Utiliza ramas paralelas con roles muy definidos:

* `main`: Versiones en producción.
* `develop`: Rama de integración donde convergen las nuevas funcionalidades.
* `feature/*`: Salen de `develop` y vuelven a `develop`.
* `release/*`: Se ramifican de `develop` para preparar una versión a producción (corrección de bugs menores, ajustes de versión). Al terminar, van a `main` y a `develop`.
* `hotfix/*`: Salen directo de `main` para arreglar un fallo crítico en producción y se fusionan de vuelta a `main` y `develop`.

### C. Trunk-Based Development (Equipos de alta velocidad / DevOps avanzados)

Los desarrolladores integran su código en `main` múltiples veces al día (commits pequeños). Las funcionalidades incompletas se ocultan en producción mediante **Feature Flags** (banderas de características) para no romper la aplicación.

---

## 4. Buenas Prácticas Profesionales

1. **Commits Atómicos y Claros:** No subas un único commit gigante que diga *"cambios varios"*. Haz commits pequeños que resuelvan una sola cosa.
2. **Usa Conventional Commits:** Estandariza los mensajes de tus commits para que el equipo (y herramientas automáticas) entiendan el propósito del cambio:
* `feat: añade validación de email en el formulario de registro`
* `fix: corrige desbordamiento de memoria en el endpoint de reportes`
* `refactor: optimiza la consulta SQL de usuarios activos`
* `docs: actualiza la guía de instalación en el README`


3. **Nunca hagas `git push --force` a ramas compartidas (`main`, `develop`)**: Si necesitas reescribir historia localmente, hazlo solo en tu rama personal. Si ya la subiste y compartiste, usa `git revert` en su lugar para deshacer cambios de forma segura sin romper el historial de tus compañeros.
4. **Haz Pull antes de empezar a trabajar**: Cada mañana o antes de arrancar una tarea:
```bash
git checkout main
git pull origin main

```


Esto evita que trabajes sobre código obsoleto.