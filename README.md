# Trio
Jonathan Oliveira Bergamo
Gustavo Oliveira
Vitor Maia


# **API de Controle e Reserva de Salas de Aula**

Esta API em Django é projetada para facilitar o controle e reserva de salas de aula em uma instituição educacional. A API oferece endpoints para gerenciar salas de aula, horários de disponibilidade e reservas de salas de aula.

## **Endpoints:**

### **1. Listar todas as Salas de Aula**

- **Endpoint:** **`/api/salas/`**
- **Método:** GET
- **Descrição:** Retorna uma lista de todas as salas de aula disponíveis.

### **2. Detalhes de uma Sala de Aula**

- **Endpoint:** **`/api/salas/<id>/`**
- **Método:** GET
- **Descrição:** Retorna os detalhes de uma sala de aula específica com base no ID fornecido.

### **3. Criar uma Sala de Aula**

- **Endpoint:** **`/api/salas/criar/`**
- **Método:** POST
- **Descrição:** Cria uma nova sala de aula com os detalhes fornecidos.

### **4. Atualizar uma Sala de Aula**

- **Endpoint:** **`/api/salas/<id>/atualizar/`**
- **Método:** PUT
- **Descrição:** Atualiza os detalhes de uma sala de aula existente com base no ID fornecido.

### **5. Excluir uma Sala de Aula**

- **Endpoint:** **`/api/salas/<id>/excluir/`**
- **Método:** DELETE
- **Descrição:** Remove uma sala de aula existente com base no ID fornecido.

### **6. Listar Horários Disponíveis de uma Sala de Aula**

- **Endpoint:** **`/api/salas/<id>/horarios/`**
- **Método:** GET
- **Descrição:** Retorna uma lista de horários disponíveis para uma sala de aula específica com base no ID fornecido.

### **7. Reservar uma Sala de Aula**

- **Endpoint:** **`/api/salas/<id>/reservar/`**
- **Método:** POST
- **Descrição:** Reserva uma sala de aula específica com base no ID fornecido para um determinado horário.

### **8. Cancelar uma Reserva de Sala de Aula**

- **Endpoint:** **`/api/reservas/<id>/cancelar/`**
- **Método:** DELETE
- **Descrição:** Cancela uma reserva de sala de aula existente com base no ID fornecido.

Observações:

- Usar fluxo **git flow**
- Usar padrão repository com **mongoDB**
- Usar templates (Arquitetura MVT completa)
