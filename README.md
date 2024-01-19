# Vanskelig å ta små valg raskt?
Hvis du sliter med å ta små hverdagsvalg så er dette lille prosjektet for deg!  
Stopper du ofte opp med å tenke hva du skal ha til middag? Eller hvilken pils du skal drikke ikveld? Eller bare et generelt 50/50 valg, hvor du vil flippe en mynt, men hvem går rundt med mynter idag?  
  
I dette prosjektet skal du lage en liste over mulige utfall i et valg, også skal scriptet returnere et tilfeldig utfall til deg.  
Dette skal også med Azure functions slik at du alltid vil ha mulighet til å spørre "skyen" om hva du burde velge.

## Hvordan komme igang
### Følg guiden i lenken under
https://learn.microsoft.com/en-us/training/modules/develop-azure-functions/5-create-function-visual-studio-code  
NB! Hvis du får problemer med at VSCode ikke gjenkjenner Microsoft pakkene etter å ha installert alt, prøv å lukke hele VSCode og starte på nytt.  
Hvis det fortsatt ikke funker prøv denne kommandoen i terminal (Høyreklikk på mappen også velg "open in integrated terminal"):
```
dotnet restore --force-evaluate
```

Etter dette kan du begynne med utvidelser!

## Utvidelser
Koden din vil se ca sånn her ut etter å ha fulgt guiden over: 
```
public static async Task<IActionResult> Run(
     [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post", Route = null)] HttpRequest req,
     ILogger log)
 {
     log.LogInformation("C# HTTP trigger function processed a request.");

     string name = req.Query["name"];

     string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
     dynamic data = JsonConvert.DeserializeObject(requestBody);
     name = name ?? data?.name;

     string responseMessage = string.IsNullOrEmpty(name)
         ? "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."
         : $"Hello, {name}. This HTTP triggered function executed successfully.";

     return new OkObjectResult(responseMessage);
 }

```
Det første du gjør er å fjerne denne linjen:
``` 
string responseMessage = string.IsNullOrEmpty(name)
? "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."
: $"Hello, {name}. This HTTP triggered function executed successfully.";
```

Neste steg er å lage listene med utfall. Å lage lister i C# ser slik ut:
```
var mat = new List<string>{ "Pizza","Taco","Pasta","Børek","Kebab","Brød"};          
```
Dette er en liste som heter "mat" og inneholder seks "string" objekter.
Du kan legge til og fjerne så mange mattretter som du vil.  
Listen "mat" er ment for å velge hva man skal ha til middag. Hvis det er andre valg som også vil ha med, er det bare å lage flere lister og fylle dem med hvilket utfall du vil ha.  
Her er noen eksempel lister:
```
var mat = new List<string>{ "Pizza","Taco","Pasta","Børek","Kebab","Brød"};
var gjøre = new List<string>{ "Sove","Lese","Gå ut","Sove","Chille","Sove"};
var mynt  = new List<string>{ "Kron","Mynt"};
var pils = new List<string>{ "Ringnes","Schous", "Tuborg", "Frydenlund", "Carlsberg", "Aass", "Hansa", "Billigste", "Ny","Isbjørn"};
```
Etter å ha laget listene så trenger vi et Random objekt. Det er dette objektet som velger et tilfeldig tall.  
Dette objektet lager du lett slik:
```
var random = new Random();
```
Dette er objekt som er i C# sin "System" pakke, og må derfor importeres ved å legge til linjen med kode under. Denne linjen skal legges helt øverst i filen med kode med de andre "using" linjene.
```
using System;
```
Etter dette trenger vi en index som er et integer. Putt denne linjen under der vi lagde random.
```
int index = 0;
```
Nå kommer vi til delen hvor koden skal velge et tilfeldig utfall fra hver av listene.

```
switch(name.ToLower()){
    case "middag":
     index = random.Next(mat.Count);
     return new OkObjectResult(mat[index]);

    case "gjøre":
     index = random.Next(gjøre.Count);
     return new OkObjectResult(gjøre[index]);

    case "mynt":
     index = random.Next(mynt.Count);
     return new OkObjectResult(mynt[index]);

    case "pils":
     index = random.Next(pils.Count);
     return new OkObjectResult(pils[index]);                
}
```
Denne koden kjører basert på hvilken verdi "name" har. Dette er en string som sendes av brukeren. Hvis den har verdien "middag" vil de 3 linjene under kjøre.
``` 
case "middag":
     index = random.Next(mat.Count);
     return new OkObjectResult(mat[index]);
```
Den første linjen genererer en tilfeldig verdi fra 0 til mat.Count verdien. mat.count verdien er antall elementer i listen mat. Fra eksempelet over vil denne verdien være 6.  
De andre casene vil gjøre det samme. Hvis du har laget en egen liste må du lage en tilsvarende case for det.

Til slutt så legger vi til en default response. Fjern først den gamle "return OkObjectResult"  også legg til denne linjen under helt til slutt (Husk å legge den utenfor krøllparentesene i Switchen):

```
return new OkObjectResult("Brukbare kommandoer er: middag, gjøre, mynt, pils");
```
Denne meldigen blir returnert når meldingen ikke inneholder noen verdi for "name". Oppdater den med dine nye kommandoer(switch cases) som du har laget!  

## Send den til Azure functions
- Lag en ny "FunctionApp" i Azure, som du gjorde i microsoft guiden tidligere
- Gå til "Workspace" også klikk på "Azure functions" knappen. Det er knappen med Lyn inni to blåe krokodilletegn.
- Velg Deploy to Function App
- Velg den nye FunctionAppen du nettop lagde.
- Gå til resources også velg riktig FunctionApp og høyreklikk på klassen under mappen "Functions". Og klikk Execute function nå.
- Erstatt Azure med kommandoen du vil utføre, i pop-up boksen som kommer opp.

Du kan også kjøre den direkte i nettleser eller med Postman med å gå den riktige URLen.  
URLen finner du slik:
- Gå til portal.azure.com
- Klikk på Function App (Søk i feltet øverst hvis du ikke finner det)
- Klikk på FunctionAppen navnet du lagde istad
- Under Overview vil det være listet opp funksjonen du nettop deployet, klikk på den
- Klikk på "Get function URL" knappen og kopier lenken
- Lim den inn i nettleseren og legg til name og kommando på slutten og trykk enter. Som eksempelet under
```
name=mynt
```
Vanligvis er URLen formatert slik:
```
https://{NavnetDuGaFunctionAppenDin}.azurewebsites.net/api/{NavnetPåFunksjonenDin}?name={Kommando}
```
Hvor du erstatter verdiene i krøll-parentesene med dine egne verdier.  
**NB! For å kjøre funksjonen din på mobil, så må du bruke URLen.**

## Videre utvikling
Nå kan du videreutvikle programmet akkurat hvordan du vil!  
Vil du legge til flere lister og kommandoer? Kanskje du heller bruke dette til å gjøre noe helt annet? 
  


### Full kode
```
using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using System.Collections.Generic;
using System;
using System.Collections.Generic;

namespace My.Function
{
    public static class HttpTrigger
    {
        [FunctionName("HttpTrigger")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post", Route = null)] HttpRequest req,
            ILogger log)
        {
            log.LogInformation("C# HTTP trigger function processed a request.");

            string name = req.Query["name"];

            string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            dynamic data = JsonConvert.DeserializeObject(requestBody);
            name = name ?? data?.name;


            var random = new Random();
            var mat = new List<string>{ "Pizza","Taco","Pasta","Børek","Kebab","Brød"};
            var gjøre = new List<string>{ "Sove","Lese","Gå ut","Sove","Chille","Sove"};
            var mynt  = new List<string>{ "Kron","Mynt"};
            var pils = new List<string>{ "Ringnes","Schous", "Tuborg", "Frydenlund", "Carlsberg", "Aass", "Hansa", "Billigste", "Ny","Isbjørn"};
            
            int index = 0;
           switch(name.ToLower()){
                case "middag":
                    index = random.Next(mat.Count);
                    return new OkObjectResult(mat[index]);

                case "gjøre":
                    index = random.Next(gjøre.Count);
                return new OkObjectResult(gjøre[index]);

                case "mynt":
                    index = random.Next(mynt.Count);
                return new OkObjectResult(mynt[index]);

                case "pils":
                    index = random.Next(pils.Count);
                return new OkObjectResult(pils[index]);                

           }
            return new OkObjectResult("Brukbare kommandoer er: middag, gjøre, mynt, pils");

        }
    }
}

```
