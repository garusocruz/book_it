# Configurações HTTP personalizadas

# Definir o tamanho máximo do corpo da resposta HTTP a ser analisado
redef HTTP::max_entity_body_length = 10MB;

# Habilitar a extração de arquivos do tráfego HTTP
redef HTTP::extraction_enabled = T;

# Definir o diretório de destino para os arquivos extraídos
redef HTTP::extraction_prefix = "/usr/local/zeek/http_files";

# Definir os tipos MIME para os quais os arquivos serão extraídos
redef HTTP::extraction_mime_types += {
    "application/zip",
    "application/pdf",
    "application/msword",
    "application/vnd.ms-excel",
    "application/vnd.ms-powerpoint",
    "application/x-rar-compressed",
    "application/octet-stream"
};

# Habilitar o armazenamento de conteúdo HTTP em texto simples
redef HTTP::store_content = T;

# Definir o diretório de destino para os conteúdos HTTP armazenados
redef HTTP::store_dir = "/usr/local/zeek/http_content";