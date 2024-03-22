# Evento para registrar cabeçalhos HTTP
event http_header(c: connection, is_orig: bool, name: string, value: string)
{
    print fmt("HTTP Header: %s: %s", name, value);
}