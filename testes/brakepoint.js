// Salvar a função original para acessar os cookies
const originalCookieSetter = Document.prototype.__lookupSetter__('cookie');
const originalCookieGetter = Document.prototype.__lookupGetter__('cookie');

// Definir o novo comportamento para definir cookies
Object.defineProperty(document, 'cookie', {
    set: function(value) {
        // Colocar um breakpoint aqui para depurar quando o cookie for modificado
        debugger; // Instrução que cria um breakpoint

        console.log('Cookie modificado:', value);

        // Chamar o comportamento original
        originalCookieSetter.call(document, value);
    },
    get: function() {
        // Retornar o valor original do cookie
        return originalCookieGetter.call(document);
    }
});
