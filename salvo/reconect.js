// URL do WebSocket
const url = 'wss://orproxy.graalonline.com:1248/logineraweb1.graalonline.com';

// Opções de subprotocolos (neste caso, "binary" foi usado)
const protocols = ['binary'];

// Criar uma nova conexão WebSocket
const socket = new WebSocket(url, protocols);

// Evento para quando a conexão for aberta
socket.addEventListener('open', () => {
    console.log('Conexão WebSocket estabelecida.');
    
    // Você pode enviar mensagens para o servidor após a conexão ser aberta
    // socket.send('Sua mensagem aqui');
});

// Evento para quando uma mensagem for recebida
socket.addEventListener('message', (event) => {
    console.log('Mensagem recebida do servidor:', event.data);
});

// Evento para quando a conexão for fechada
socket.addEventListener('close', () => {
    console.log('Conexão WebSocket fechada.');
});

// Evento para lidar com erros na conexão
socket.addEventListener('error', (error) => {
    console.error('Erro no WebSocket:', error);
});
