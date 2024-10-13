// Verifica se a variável 'canvas' já foi declarada
if (typeof canvas === 'undefined') {
    const canvas = document.getElementById('unity-canvas');
} else {
    // Se a variável já existir, apenas reutilize o elemento
    canvas = document.getElementById('unity-canvas');
}

const gl = canvas.getContext('webgl') || canvas.getContext('webgl2');

if (!gl) {
    console.error('Seu navegador não suporta WebGL.');
} else {
    console.log('Contexto WebGL encontrado com sucesso.');
}







































function restartCanvas() {
    const oldCanvas = document.getElementById('unity-canvas');
    const parent = oldCanvas.parentNode;

    // Criar um novo elemento <canvas>
    const newCanvas = document.createElement('canvas');
    newCanvas.id = 'unity-canvas'; // Manter o mesmo ID
    newCanvas.width = oldCanvas.width;
    newCanvas.height = oldCanvas.height;

    // Substituir o canvas antigo pelo novo
    parent.replaceChild(newCanvas, oldCanvas);

    // Obter o novo contexto WebGL
    const gl = newCanvas.getContext('webgl') || newCanvas.getContext('webgl2');
    if (!gl) {
        console.error('Falha ao criar o novo contexto WebGL.');
        return;
    }

    console.log('Canvas reiniciado com sucesso.');

    // Opcional: reiniciar o jogo ou refazer configurações
    iniciarJogo(gl); // Chamar uma função para reiniciar o jogo ou reconfigurar
}

// Exemplo de uso
restartCanvas();









// Função para monitorar mudanças nos cookies
let lastCookie = document.cookie;
setInterval(() => {
    let currentCookie = document.cookie;
    if (currentCookie !== lastCookie) {
        console.log('Cookie modificado:', currentCookie);
        lastCookie = currentCookie;
    }
}, 1000); // Verifica mudanças a cada 1 segundo