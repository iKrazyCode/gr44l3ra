
// usado no tampermonkey para iniciar antes que a página e efazer leitura de todos websockets


(function() {
    'use strict';

    // Array global para armazenar as conexões WebSocket
    window.allSockets = [];

    // Função para interceptar a criação de novos WebSockets
    (function() {
        // Salva o construtor original do WebSocket
        const OriginalWebSocket = window.WebSocket;

        // Cria um novo construtor de WebSocket que intercepta as conexões
        window.WebSocket = function(...args) {
            const ws = new OriginalWebSocket(...args);
            ws._url = args[0];
            ws._protocols = args[1];
            window.allSockets.push(ws);
            return ws;
        };

        // Copia as propriedades estáticas e o protótipo
        window.WebSocket.prototype = OriginalWebSocket.prototype;
        window.WebSocket.CONNECTING = OriginalWebSocket.CONNECTING;
        window.WebSocket.OPEN = OriginalWebSocket.OPEN;
        window.WebSocket.CLOSING = OriginalWebSocket.CLOSING;
        window.WebSocket.CLOSED = OriginalWebSocket.CLOSED;
    })();

    // Função para fechar todas as conexões WebSocket ativas
    window.closeAllWebSockets = function() {
        window.allSockets.forEach(function(ws) {
            if (ws.readyState === WebSocket.OPEN || ws.readyState === WebSocket.CONNECTING) {
                ws.close();
                console.log('WebSocket fechado:', ws);
            }
        });
    };
})();