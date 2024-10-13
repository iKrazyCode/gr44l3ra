function brut(pk) {
    // Para usar essa função, tem que antes estar usando o script do tampermonkey

    let nome = '/idbfs/33b28fcee7db5511f69dba35d2c3830a/files/creationtime.dat'; // Defina o valor que deseja atribuir ao cookie
    let dataExpiracao = "Fri, 31 Dec 9999 23:59:59 GMT"; // Expiração do cookie

    // Define o cookie com o valor de 'pk'
    document.cookie = `${nome}=${pk}; expires=${dataExpiracao}; path=/`;

    // Exclui o cookie 'nickname_new' definindo uma data de expiração no passado
    document.cookie = 'nickname_new=nao_existe; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';

    // Itera sobre todos os sockets em 'allSockets'
    for (let i of allSockets) {
        if (i.url.includes('192.99.218.229')) {
            i.close();
        }
    }
    // Limpa o array de sockets
    allSockets = [];

    document.getElementById('unity-canvas').click();
};
