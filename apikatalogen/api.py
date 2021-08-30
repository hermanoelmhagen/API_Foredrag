# Alla rader som börjar med ett hashtag-tecken (#) räknas som kommentar (i programmeringsspråket Python), alltså något
# som inte försöker köras av kompilator eller interpreter. Detta används för att
# göra koden läsbar för nästa person som ska läsa den, alternativt för sig själv.
# Kod blir ofta väldigt komplex och därför är det väldigt bra att dokumentera vad man gör!

# Här importerar vi bibliotek. I sin grund är det egentligen en samling av funktioner och kod
# som enkelt kan importeras till sin egna kod utan att man behöver skriva den själv eller 
# copypastea in den i sin egna kod. 
# Enkelt beskrivet så kan man säga att när man känner att det känns onödigt att återuppfinna hjulet
# så kan man använda sig utav bibliotek. Oftast har någon redan skapat funktioner du behöver.
# Dock så kan det i inlärningssyfte vara väldigt användbart att faktiskt grotta ner sig i grunden kring
# koden man importerar, eller att försöka återskapa funktioner som man tycker är användbara!

# Biblioteket requests är väldigt användbart för att utföra GET, POST, PUT och DELETE requests
# mot API:er. Som ni kan se så är det väldigt liten mängd kod, detta tack vare bibliotek som gör
# "the heavy lifting".
import requests

# pprint (pretty print) är mest ett bibliotek som används för estetik. Ibland när man "printar" ut (visar data i kommandotolk eller annan konsol)
# så blir det väldigt grötigt. pprint gör ett försök till att identifiera VAD det är för typ av
# text du vill printa ut och gör om det till ett rimligt format att kolla på.
import pprint

# Här definierar vi vilken "API-endpoint" vi vill göra en request till och sparar det i variabeln "URL". 
# Helt enkelt VART vi vill ställa vår fråga.
URL = "http://api.apikatalogen.se/v1/sources"

# Här låter vi biblioteket requests hjälpa oss att skicka en "GET"-förfrågan till vår API-endpoint som är sparad i
# variabeln "URL". Responsen från denna förfrågan sparar vi i variabeln "request_response".  
request_response = requests.get(URL)

# Här låter vi bilblioteket pprint hjälpa oss att se till att utskriften i vår konsol blir mer läsbar.
# Förväntat resultat här är att din konsol visar vilka API:n som hemsidan "apikatalogen.se" har i sin databas
# över användbara svenska API:n.
pprint.pprint(request_response.text)
