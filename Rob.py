try:
    from chatterbot import ChatBot
    from chatterbot.trainers import ListTrainer
    import speech_recognition as sr
    from gtts import gTTS
    from playsound import playsound
except ImportError:
    print("Erro ao importar módulo")


def ouvir_som():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Microfone...")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
        except sr.UnknownValueError:
            print("Bot: Isso não funcionou...")

def cria_audio(audio):
    tts = gTTS(audio, language='pt-BR')
    tts.save("Bot.mp3")
    playsound("Bot.mp3")


bot = ChatBot('Chat')

conversas = ["oi",'olá!','Tudo bem?','Tudo e contigo','Eu tou bem','Que bom','Qual a melhor linguagem?','a melhor é python']

trainer = ListTrainer(bot)
trainer.train(conversas)

while True:
    quest = input("Humano: ")
    resposta = bot.get_response(quest)
    print("Bot: ",resposta)
    

