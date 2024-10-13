// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      2024-10-13
// @description  try to take over the world!
// @author       You
// @match        https://era.graalonline.com/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=graalonline.com
// @grant        none
// ==/UserScript==


// PLUGIN


(function() {
    'use strict';

    window.allSockets = [];

    (function() {
        const OriginalWebSocket = window.WebSocket;

        function CustomWebSocket(...args) {
            const ws = new OriginalWebSocket(...args);
            ws._url = args[0];
            ws._protocols = args[1];
            ws._listeners = {};
            ws._initialSentMessages = []; // Mensagens enviadas antes da resposta do servidor
            ws._serverResponded = false;  // Flag para indicar se o servidor já respondeu

            // Intercepta o método send para armazenar mensagens iniciais
            const originalSend = ws.send;
            ws.send = function(data) {
                if (!ws._serverResponded) {
                    ws._initialSentMessages.push(data);
                }
                originalSend.call(ws, data);
            };

            // Intercepta o evento onmessage para detectar a primeira resposta do servidor
            ws.addEventListener('message', function(event) {
                if (!ws._serverResponded) {
                    ws._serverResponded = true;
                }
            });

            // Armazena event listeners personalizados
            const originalAddEventListener = ws.addEventListener;
            ws.addEventListener = function(type, listener, options) {
                if (!ws._listeners[type]) {
                    ws._listeners[type] = [];
                }
                ws._listeners[type].push(listener);
                return originalAddEventListener.call(ws, type, listener, options);
            };

            // Armazena event listeners diretos (onopen, onmessage, etc.)
            ['onopen', 'onmessage', 'onerror', 'onclose'].forEach(function(eventType) {
                let originalListener = ws[eventType];
                Object.defineProperty(ws, eventType, {
                    get: function() {
                        return originalListener;
                    },
                    set: function(listener) {
                        if (originalListener) {
                            ws.removeEventListener(eventType.slice(2), originalListener);
                        }
                        originalListener = listener;
                        if (listener) {
                            ws.addEventListener(eventType.slice(2), listener);
                        }
                    },
                    enumerable: true,
                    configurable: true
                });
            });

            window.allSockets.push(ws);
            return ws;
        }

        // Copia o protótipo e propriedades estáticas
        CustomWebSocket.prototype = OriginalWebSocket.prototype;
        CustomWebSocket.CONNECTING = OriginalWebSocket.CONNECTING;
        CustomWebSocket.OPEN = OriginalWebSocket.OPEN;
        CustomWebSocket.CLOSING = OriginalWebSocket.CLOSING;
        CustomWebSocket.CLOSED = OriginalWebSocket.CLOSED;

        window.WebSocket = CustomWebSocket;
    })();

    // Função para replicar um socket enviando apenas as mensagens iniciais
    window.replicarSocket = function(originalSocket) {
        if (!originalSocket || !originalSocket._url) {
            console.error("O socket original não possui informações suficientes para replicação.");
            return null;
        }

        // Cria um novo WebSocket com a mesma URL e protocolos
        const newSocket = originalSocket._protocols
            ? new WebSocket(originalSocket._url, originalSocket._protocols)
            : new WebSocket(originalSocket._url);

        // Copia as propriedades
        newSocket._url = originalSocket._url;
        newSocket._protocols = originalSocket._protocols;
        newSocket._listeners = originalSocket._listeners || {};
        newSocket._initialSentMessages = originalSocket._initialSentMessages || [];

        // Reanexa os event listeners personalizados
        for (const type in originalSocket._listeners) {
            if (originalSocket._listeners.hasOwnProperty(type)) {
                originalSocket._listeners[type].forEach(function(listener) {
                    newSocket.addEventListener(type, listener);
                });
            }
        }

        // Reatribui event listeners diretos
        ['onopen', 'onmessage', 'onerror', 'onclose'].forEach(function(eventType) {
            const listener = originalSocket[eventType];
            if (listener) {
                newSocket[eventType] = listener;
            }
        });

        // Envia as mensagens iniciais após a conexão ser estabelecida
        newSocket.addEventListener('open', function() {
            console.log('Socket replicado conectado. Reenviando mensagens iniciais...');
            newSocket._initialSentMessages.forEach(function(message) {
                newSocket.send(message);
                console.log('Mensagem inicial reenviada:', message);
            });
        });

        return newSocket;
    };
})();