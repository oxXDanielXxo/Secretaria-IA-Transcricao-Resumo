# 🎙️ Assistente Virtual Privacy-First (Speech-to-Text & NLP Extrativo)

Um pipeline completo de Inteligência Artificial para processamento de áudio e extração de contexto semântico. Desenvolvido em Python, o sistema foca em privacidade (Privacy-First), operando localmente sem a necessidade de enviar o texto transcrito para APIs de IAs Generativas externas (como ChatGPT).

## ⚙️ Tecnologias e Arquitetura
* **Linguagem:** Python
* **Speech-to-Text (ASR):** `SpeechRecognition` para manipulação acústica (limpeza de ruído ambiente) e transcrição de arquivos `.wav` em texto contínuo.
* **Processamento de Linguagem Natural (NLP):** Biblioteca `nltk` (Natural Language Toolkit) para tokenização léxica em Português e `sumy` para a modelagem matemática.
* **Algoritmo de Resumo:** Implementação do modelo Extrativo **LSA (Latent Semantic Analysis)**, que utiliza decomposição em valores singulares para identificar os tópicos latentes mais relevantes no texto e extrair as frases com maior densidade semântica.

## 🚀 Funcionalidades de Engenharia
* **Transcrição Assíncrona de Áudio:** Conversão de voz para texto com tratamento prévio de ruído de fundo via `adjust_for_ambient_noise`.
* **Motor Lógico Anti-Falhas (Edge Case Handling):** IAs de transcrição frequentemente retornam "blocos maciços" de texto sem pontuação (fluxo contínuo) ou com pontuações isoladas dentro de números, o que cega motores de NLP extrativos. O script possui um sistema algorítmico que detecta a ausência de delimitações de frase reais e injeta pontuações corretivas baseadas em densidade de palavras, garantindo que o motor matemático consiga operar.
* **Ata Executiva Automática:** Ao invés de usar LLMs pesados e propensos a "alucinações", o sistema foca em eficiência matemática pura, gerando resumos baseados estritamente no que foi falado (sem inventar contexto).

## 💻 Como Executar
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Substitua ou insira seu próprio arquivo de áudio (`reuniao.wav`) no diretório principal.
4. Execute o motor: `python transcritor.py`
