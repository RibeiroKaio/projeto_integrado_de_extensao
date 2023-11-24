from LeIA import SentimentIntensityAnalyzer 

def AnaliseDeSentimentos(texto):
    cont=0
    var=str()
    s = SentimentIntensityAnalyzer()

    #texto=str(s.polarity_scores('quero comer pizza'));
    texto=str(s.polarity_scores(texto));

    for i in list(texto):
        if i=='d':
            cont=1;
        elif i==' 'and cont==1:
            cont=2;
        elif cont==2 and i!='}':
            var=str(var)+str(i);

    # print(var + senti)
    outro=float(var)

    return outro;


def sentimento(outro):
    if outro >=0.05:
        #print("positivo");
        return "positivo";

    elif outro<=-0.05:
        #print("negativo");
        return "negativo";

    elif outro > -0.05 and outro <0.05:
        #print("neutro");
        return "neutro";

    else:
        #print("Nunca é pra aparecer isso");
        return "Nunca é pra aparecer isso";


