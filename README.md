# API de Validação de Atestados Médicos

## Descrição

Essa é a prova de conceito de uma API desenvolvida em **FastAPI** que compara dois nomes e retorna um índice de similaridade baseado em dois algoritmos: **Levenshtein Distance** e **Jaro-Winkler**.

Caso a prova de conceito seja aprovada, iremos seguir a seguinte [Especificação da API de Validação de Atestados Médicos](https://docs.google.com/document/d/1YmPguLRIdmh7hrVrABcd93Az02iWd7tSQb3YloPSlTE/edit?tab=t.0#heading=h.uu1ce14y1c43)

## Tecnologias Utilizadas

- **Python 3**
- **FastAPI**
- **FuzzyWuzzy**
- **Uvicorn**

## Como Executar

1. Instale as dependências:
   ```sh
   pip install fastapi uvicorn fuzzywuzzy
   ```
2. Execute a API:
   ```sh
   uvicorn script_name:app --reload
   ```
   Substitua `script_name` pelo nome do seu arquivo Python.

## Como Funciona a Comparação de Nomes

A API utiliza dois algoritmos principais para calcular a similaridade entre os nomes:

### Levenshtein Distance

O algoritmo de **Levenshtein Distance** mede a diferença entre duas strings calculando o número mínimo de operações necessárias para transformar uma string na outra. As operações permitidas são inserção, deleção e substituição de caracteres. Quanto menor a distância, maior a similaridade entre os nomes.

### Jaro-Winkler

O **Jaro-Winkler** é um algoritmo projetado para medir a similaridade entre strings, dando mais peso para correspondências nos primeiros caracteres. Isso o torna mais eficiente para comparar nomes próprios, pois pequenas variações no final da palavra têm menos impacto na pontuação final.

A API combina ambos os algoritmos com pesos iguais para gerar uma pontuação final de similaridade.

## Como Testar

### Via cURL

```sh
curl -X 'POST' 'http://127.0.0.1:8000/compare-names/' \
     -H 'Content-Type: application/json' \
     -d '{"name1": "Gabriel", "name2": "Gabriel Mesquita"}'
```

### Via Postman

1. Selecione **POST**
2. Insira a URL: `http://127.0.0.1:8000/compare-names/`
3. No **Body**, escolha **raw** e selecione **JSON**
4. Insira:
   ```json
   {
       "name1": "Gabriel",
       "name2": "Gabriel Mesquita"
   }
   ```
5. Clique em **Send**

### Via Python

```python
import requests

url = "http://127.0.0.1:8000/compare-names/"
data = {"name1": "Gabriel", "name2": "Gabriel Mesquita"}

response = requests.post(url, json=data)
print(response.json())
```

## Exemplo de Resposta

```json
{
    "similarity": 0.86
}
```
