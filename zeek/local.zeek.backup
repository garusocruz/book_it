@load protocols/http
redef Http::config_file = "local-http-config.zeek";

event zeek_init()
{
    print "Starting HTTP analyzer";
    HTTP::enableAnalyzer();
}

event http_request(c: connection, method: string, uri: string, version: string, headers: table[string] of string, body: string)
{
    if (uri == "/api/users/v1") {
        print fmt("HTTP Request to /api/users/v1: %s %s", method, uri);
        
        # Verificar se o método da solicitação é inválido ou não autorizado
        if (method != "GET" && method != "POST") {
            print fmt("Invalid request method: %s", method);
            # Adicione ações relevantes, como registrar ou alertar sobre a solicitação inválida.
        }
        
        # Analisar os cabeçalhos da solicitação em busca de padrões de ataques conhecidos
        for (h in headers) {
            if (h in /.*(exec|system|cmd).*/) {
                print fmt("Suspicious header detected: %s", h);
                # Adicione ações relevantes, como registrar ou alertar sobre o cabeçalho suspeito.
            }
        }

        # Validar os parâmetros da solicitação para evitar ataques de injeção ou exploração
        if (|body| > 0) {
            if (body !/^[a-zA-Z0-9]*$/) {
                print "Invalid characters detected in request body";
                # Adicione ações relevantes, como registrar ou rejeitar a solicitação com base na validação do corpo.
            }
        }

        # Aqui você pode adicionar mais regras de segurança, dependendo das suas necessidades específicas.
    }
}
