function criarCookie(id) {
    let nome = '/idbfs/33b28fcee7db5511f69dba35d2c3830a/files/creationtime.dat'; // Defina o valor que deseja atribuir ao cookie
    let dataExpiracao = "Fri, 31 Dec 9999 23:59:59 GMT"; // Expiração do cookie
    document.cookie = `${nome}=${id}; expires=${dataExpiracao}; path=/`;
    document.cookie = 'nickname_new=;expires=Thu, 01 Jan 1970 00:00:00 UTC;';
    window.location = window.location;
}
criarCookie('1728616085.70900011');