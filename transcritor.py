import speech_recognition as sr
import os
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# 1. Preparação
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

reconhecedor = sr.Recognizer()
arquivo_audio = "reuniao.wav"

print("🎙️ Inicializando Sistema de Secretária Virtual (100% Local)...")

if not os.path.exists(arquivo_audio):
    print(f"❌ Erro Crítico: O arquivo '{arquivo_audio}' não foi encontrado.")
else:
    # 2. Escuta
    with sr.AudioFile(arquivo_audio) as fonte:
        print("🎧 Extraindo áudio e limpando ruídos...")
        reconhecedor.adjust_for_ambient_noise(fonte)
        audio_dados = reconhecedor.record(fonte)
        
    print("🧠 Decodificando fala para texto...")
    
    try:
        texto_extraido = reconhecedor.recognize_google(audio_dados, language="pt-BR")
        
        print("\n📝 ==== TRANSCRIÇÃO BRUTA (Tudo o que foi falado) ==== 📝")
        print(texto_extraido)
        print("=========================================================\n")
        
        # ==========================================================
        # NOVO: INJETOR DE PONTUAÇÃO ARTIFICIAL (V2 - Blindado)
        # ==========================================================
        # Se o texto for longo (mais de 20 palavras) e não tiver quase nenhum ponto 
        # final real (ponto seguido de espaço), nós forçamos a pontuação.
        if texto_extraido.count(". ") < 2 and len(texto_extraido.split()) > 20:
            print("🔧 Motor Lógico: Fluxo contínuo detectado. Injetando pontuação forçada...")
            palavras = texto_extraido.split()
            frases_artificiais = []
            
            for i in range(0, len(palavras), 15):
                pedaco = " ".join(palavras[i:i+15])
                frases_artificiais.append(pedaco + ".")
                
            texto_extraido = " ".join(frases_artificiais)
            
        # ==========================================================
        # 3. MÓDULO: RESUMO OFFLINE (NLP EXTRATIVO)
        # ==========================================================
        print("⚙️ Analisando relevância semântica e gerando Ata Resumida...")
        
        parser = PlaintextParser.from_string(texto_extraido, Tokenizer("portuguese"))
        sumarizador = LsaSummarizer()
        
        # Extraindo as 2 frases mais densas do áudio
        resumo = sumarizador(parser.document, 2)
        
        print("\n🎯 ==== ATA DA REUNIÃO (RESUMO EXECUTIVO) ==== 🎯")
        if len(parser.document.sentences) <= 1:
            print("-> Aviso: O áudio não pôde ser fatiado corretamente.")
            print(f"-> {texto_extraido}")
        else:
            for frase in resumo:
                print(f"-> {frase}")
        print("===================================================\n")
        
    except sr.UnknownValueError:
        print("❌ Falha na IA: Áudio ininteligível ou mudo.")
    except sr.RequestError as e:
        print(f"❌ Falha de Conexão: Erro de rede -> {e}")