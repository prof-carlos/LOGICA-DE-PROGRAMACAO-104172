# DS - Backend

## Configuração de variáveis de ambiente

Antes de iniciar o projeto, defina as variáveis de ambiente necessárias:

- SPRING_APP_NAME (opcional, padrão: aula)
- JPA_DDL_AUTO (opcional, padrão: update)
- DB_URL (obrigatório)
- DB_USERNAME (obrigatório)
- DB_PASSWORD (obrigatório)
- DB_DRIVER (opcional, padrão: com.mysql.cj.jdbc.Driver)
- JPA_SHOW_SQL (opcional, padrão: true)

Exemplo de export no Linux:
```bash
export DB_URL="jdbc:mysql://localhost:3306/seubanco"
export DB_USERNAME="usuario"
export DB_PASSWORD="senha"
```

## Inicialização

Execute o projeto normalmente após definir as variáveis:
```bash
./mvnw spring-boot:run
```