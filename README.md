# Subdomain Resolver

## Descrição

O **Subdomain Resolver** é uma ferramenta simples escrita em Python para auxiliar na enumeração de subdomínios através de resolução DNS.

A ferramenta recebe um domínio-alvo e uma wordlist contendo possíveis nomes de subdomínio. Para cada entrada, realiza consultas DNS utilizando a biblioteca `socket` para verificar a existência de registros IPv4 (A) e IPv6 (AAAA).

O objetivo é identificar subdomínios válidos, contribuindo para a fase de reconhecimento (Reconnaissance) de um teste de invasão autorizado.

Este projeto foi desenvolvido como exercício de estudo do curso **Python para Pentesters**, ministrado por **Messias Eric**.

## Objetivo

Auxiliar na identificação de subdomínios ativos por meio de resolução DNS, ampliando a superfície de ataque conhecida durante atividades de reconhecimento.

## Funcionalidades

- Enumeração de subdomínios utilizando uma wordlist.
- Resolução de registros IPv4.
- Resolução de registros IPv6.
- Exibição apenas dos subdomínios que possuem resolução válida.

## Estrutura

```
.
├── main.py
└── src
    └── resolver.py
```

## Requisitos

- Python 3.10 ou superior

Nenhuma biblioteca externa é necessária.

## Uso

```bash
python main.py <host> <wordlist>
```

### Exemplo

```bash
python main.py example.com subdomains.txt
```

Se `subdomains.txt` contiver:

```
www
mail
api
admin
dev
```

A ferramenta realizará consultas para:

```
www.example.com
mail.example.com
api.example.com
admin.example.com
dev.example.com
```

## Saída

Exemplo:

```
www.example.com        IPV4 - 93.184.216.34
www.example.com        IPV6 - 2606:2800:220:1:248:1893:25c8:1946
mail.example.com       IPV4 - 192.168.1.10
```

Subdomínios sem resolução DNS não são exibidos.

## Limitações

- Não realiza consultas DNS diretas; utiliza o resolvedor configurado no sistema operacional.
- Não identifica wildcards DNS.
- Não realiza consultas paralelas.
- Não diferencia tipos de registros além de IPv4 e IPv6.
- Não implementa tratamento de rate limiting ou timeout personalizado.

## Aviso

Esta ferramenta deve ser utilizada exclusivamente em ambientes autorizados ou para fins educacionais. O usuário é responsável por garantir que possui permissão para realizar atividades de reconhecimento no domínio-alvo.

## Créditos

Projeto desenvolvido como exercício do curso **Python para Pentesters**, de **Messias Eric**.
