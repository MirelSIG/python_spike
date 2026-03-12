let pyodideReadyPromise = null;
const promptHTML = '<span class="terminal-user">mirel@python-dev</span>:<span class="terminal-path">~/proyecto</span>$ ';
let currentExample = 'strings';
let currentFile = './metodos-strings/strings_basicos.py';

async function initPyodide() {
    if (!pyodideReadyPromise) {
        try {
            pyodideReadyPromise = loadPyodide();
            await pyodideReadyPromise;
        } catch (err) {
            console.error("Error al cargar Pyodide", err);
        }
    }
}

async function cargarEjemplo(tipo) {
    if (tipo === 'strings') {
        currentExample = 'strings';
        currentFile = './metodos-strings/strings_basicos.py';
        document.getElementById('example-title').innerHTML = 'Ejemplo: Métodos de <code>Strings</code> en Python';
    } else if (tipo === 'listas') {
        currentExample = 'listas';
        currentFile = './metodos-listas/listas_basicas.py';
        document.getElementById('example-title').innerHTML = 'Ejemplo: Métodos de <code>Listas</code> en Python';
    } else if (tipo === 'pathlib') {
        currentExample = 'pathlib';
        currentFile = './metodos-pathlib/pathlib_basicos.py';
        document.getElementById('example-title').innerHTML = 'Ejemplo: Uso básico de <code>pathlib</code> en Python';
    } else if (tipo === 'pathlib-rutas') {
        currentExample = 'pathlib-rutas';
        currentFile = './metodos-pathlib/pathlib_rutas.py';
        document.getElementById('example-title').innerHTML = 'Ejemplo: Navegación de <code>rutas</code> con pathlib';
    } else if (tipo === 'pathlib-archivos') {
        currentExample = 'pathlib-archivos';
        currentFile = './metodos-pathlib/pathlib_archivos.py';
        document.getElementById('example-title').innerHTML = 'Ejemplo: Operaciones de <code>archivos</code> con pathlib';
    } else if (tipo === 'pathlib-busqueda') {
        currentExample = 'pathlib-busqueda';
        currentFile = './metodos-pathlib/pathlib_busqueda.py';
        document.getElementById('example-title').innerHTML = 'Ejemplo: <code>glob</code> y búsqueda recursiva con pathlib';
    }
    await recargarCodigo();
}

async function recargarCodigo() {
    const editor = document.getElementById('python-editor');
    if (!editor) return;
    try {
        const response = await fetch(currentFile);
        if (!response.ok) throw new Error('No se pudo leer el archivo');
        const code = await response.text();
        editor.value = code;
        editor.style.display = 'block'; // Mostrar una vez cargado
    } catch (err) {
        editor.value = "# Error al cargar el código original: " + err.message;
        editor.style.display = 'block';
    }
}

// Precargar Pyodide y el código en background si estamos en la página
document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById('python-editor')) {
        initPyodide();
        recargarCodigo();
    }
});

async function ejecutarCodigo() {
    const output = document.getElementById('terminal-output');
    const promptStart = document.getElementById('prompt-start');
    const btnRun = document.getElementById('btn-run');
    const editor = document.getElementById('python-editor');
    
    if (!editor || !output) return;

    if (promptStart) {
        promptStart.style.display = 'none';
    }
    
    const block = document.createElement('div');
    
    const cmdSpan = document.createElement('span');
    cmdSpan.className = 'terminal-cmd';
    cmdSpan.innerHTML = promptHTML + 'python3 MirelPY/' + currentFile.replace('./', '');
    
    const resSpan = document.createElement('span');
    resSpan.className = 'terminal-res';
    resSpan.innerHTML = '<span class="terminal-running">(Ejecutando...)</span>';
    
    block.appendChild(cmdSpan);
    block.appendChild(resSpan);
    output.appendChild(block);
    output.scrollTop = output.scrollHeight;
    
    if (btnRun) {
        btnRun.style.pointerEvents = 'none';
        btnRun.style.opacity = '0.5';
    }

    try {
        let pyodide = await pyodideReadyPromise;
        
        // En lugar de hacer un fetch, ahora cogemos el código directo del textarea editable.
        const codeToRun = editor.value;
        
        // Redirigimos consola
        pyodide.runPython(`
import sys
import io
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
        `);
        
        // Ejecutamos el código que el usuario escribió/editó en la web
        pyodide.runPython(codeToRun);
        
        // Obtenemos el output
        let stdout = pyodide.runPython("sys.stdout.getvalue()");
        let stderr = pyodide.runPython("sys.stderr.getvalue()");
        
        // Formateamos para HTML
        let finalOutput = stdout;
        if (stderr) finalOutput += "\n[Error]\n" + stderr;
        
        resSpan.innerHTML = finalOutput ? finalOutput.replace(/\n/g, '<br>') : '<em>(Sin salida)</em>';

    } catch (err) {
        resSpan.innerHTML = '<span style="color: #ef4444;">Error de Python:<br>' + err.toString().replace(/\n/g, '<br>') + '</span>';
    } finally {
        if (btnRun) {
            btnRun.style.pointerEvents = 'auto';
            btnRun.style.opacity = '1';
        }
        
        // Añadir nuevo prompt al final
        const newPrompt = document.createElement('span');
        newPrompt.innerHTML = promptHTML + '<span class="terminal-cursor"></span>';
        output.appendChild(newPrompt);
        
        output.scrollTop = output.scrollHeight;
    }
}

window.limpiarTerminal = function() {
    const output = document.getElementById('terminal-output');
    if (output) {
        output.innerHTML = '<span id="prompt-start">' + promptHTML + '<span class="terminal-cursor"></span></span>';
    }
};

window.ejecutarCodigo = ejecutarCodigo;
window.cargarEjemplo = cargarEjemplo;
