# Definir uma entidade HTTP para URLs
type HTTP::Url: record {
    host: string;
    path: string;
    port: port;
};