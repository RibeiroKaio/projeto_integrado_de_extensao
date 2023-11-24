import discord
from datetime import datetime , timedelta
import sys
sys.path.insert(0, ',/ads')
from ads import AnaliseDeSentimentos,sentimento


def  analisa_sentimento_no_aquivo(nickname):
    cont=0;
    sms=[];
    sent=float(0);
    global tempo_de_sentimento;

    with open("conversas","r") as arquivo:
        linhas=arquivo.readlines();
        for i in range(0, len(linhas), 3):
            data_hora = linhas[i].strip();
            nome = linhas[i + 1].strip();
            frase = linhas[i + 2].strip();
            if nome == nickname:
                data_hora = datetime.strptime(data_hora, '%Y-%m-%d %H:%M:%S')
                diferenca_tempo = datetime.now() - data_hora

                if diferenca_tempo <= timedelta(days=tempo_de_sentimento):
                    sms.append(frase);
                    cont+=1;

    for i in sms:
        sent+=AnaliseDeSentimentos(i);
        print(i);
    if cont==0:
       return str(nickname+" não encontrado");
    else:
        sent/=cont;
        print(sentimento(sent));
        return str(nickname+" sentimento "+sentimento(sent));




intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# arquivo=open("conversas","w");
# arquivo.close();


global tempo_de_sentimento;
tempo_de_sentimento=1;

@client.event
async def on_ready():
    print('esta funcinando');

@client.event
async def on_message(message):
    frase='a'; 
    pessoa='';
    global tempo_de_sentimento;
    
    if message.author == client.user:
        return

    if message.content.startswith('!azzi'):
        await message.channel.send('ola, '+str(message.author))
    
    elif message.content.startswith('!menu'):
        await message.channel.send("!azzi -\n!close - não faz nada, mas existe\n!dias_sentimento (numero) - muda a quantiade de dias a ser analisado\n!ads (nickname) - analisa os sentimentos das mensagens do usuario em um intervalo de tempo\n&(frase) - analisa a frase digitada");
    
    elif message.content.startswith('!close'):
        await message.channel.send('Isso ainda não funciona')

    elif message.content.startswith('!dias_sentimento'):
        cont=int(message.content[17:])
        if(cont>0):
            tempo_de_sentimento=cont;
        else:
            await message.channel.send("comando errado");

    elif message.content[:4]== '!ads':
        if len(message.content)>6: 
            await message.channel.send(analisa_sentimento_no_aquivo(message.content[5:]));
        else:
            await message.channel.send("nickname não digitado");

    elif message.content[:1]== '&':
        txt=AnaliseDeSentimentos(str(message.content)[1:]);
        print(sentimento(txt));
        await message.channel.send(sentimento(txt));
    
    elif frase!=message.content and pessoa!=message.author:
        arquivo=open("conversas","a");
        arquivo.write(str(datetime.now())[:19]+"\n"+str(message.author)+"\n"+str(message.content)+"\n");
        
        frase=message.content;
        #print(message.author ,message.content);# print no terminal o nome e a mensagem
        arquivo.close();
      
    print('\n')
        
      

client.run()

