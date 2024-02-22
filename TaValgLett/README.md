Note: English at the end

# Vanskelig å ta små valg raskt?

Hvis du sliter med å ta små hverdagsvalg så er dette lille prosjektet for deg!  
Stopper du ofte opp for å tenke over hva du skal ha til middag? Eller hvilken pils du skal drikke i kveld? Eller har du kanskje et 50/50 valg,der du gjerne bare skulle hatt en mynt å flippe, men hvem går vel rundt med mynter i dag?

I dette prosjektet skal du lage en liste over mulige utfall i et valg, og så skal scriptet returnere et tilfeldig utfall til deg.  
Dette skal også gjøres med Azure Function slik at du alltid vil ha mulighet til å spørre "skyen" om hva du burde velge.

## Hvordan komme i gang

###

Denne guiden er skrevet i C#, et programmeringsspråk som ligner veldig på Java.
For å kjøre dette lokalt kan du laste ned .Net herfra https://dotnet.microsoft.com/en-us/download
.Net lar deg kjøre C#.

### Følg guiden i lenken under

https://learn.microsoft.com/en-us/training/modules/develop-azure-functions/5-create-function-visual-studio-code  
NB! Hvis du får problemer med at VSCode ikke gjenkjenner Microsoft pakkene etter å ha installert alt, prøv å lukke hele VSCode og starte på nytt.  
Hvis det fortsatt ikke funker prøv denne kommandoen i terminal (Høyreklikk på mappen også velg "open in integrated terminal"):

```
dotnet restore --force-evaluate
```

Har du fulgt guiden? Da kan du begynne med utvidelser!

## Utvidelser

Koden din vil se cirka sånn her ut etter å ha fulgt guiden over:

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

Neste steg er å lage listene med utfall. Du skal lage en liste med ting å velge mellom, og legge den i stedet for det du nettopp slettet. Å lage lister i C# ser slik ut:

```
var mat = new List<string>{ "Pizza","Taco","Pasta","Børek","Kebab","Brød"};
```

Her må du nok importere lista. Dette gjør du ved å legge til linjen under helt øverst i filen med kode med de andre "using" linjene.

```
using System.Collections.Generic;
```

Dette er en liste som heter "mat" og inneholder seks "string" objekter.
Du kan legge til og fjerne så mange mattretter som du vil.  
Listen "mat" er ment for å velge hva man skal ha til middag. Hvis det er andre valg som også vil ha med, er det bare å lage flere lister og fylle dem med hvilket utfall du vil ha.  
Her er noen eksempellister:

```
var mat = new List<string>{ "Pizza","Taco","Pasta","Børek","Kebab","Brød"};
var gjøre = new List<string>{ "Sove","Lese","Gå ut","Sove","Chille","Sove"};
var mynt  = new List<string>{ "Kron","Mynt"};
var pils = new List<string>{ "Ringnes","Schous", "Tuborg", "Frydenlund", "Carlsberg", "Aass", "Hansa", "Billigste", "Ny","Isbjørn"};
```

Etter å ha laget listene så trenger vi et Random-objekt. Det er dette objektet som velger et tilfeldig tall.  
Dette lager du enkelt slik:

```
var random = new Random();
```

Dette er et objekt som er i C# sin "System" pakke, og må derfor importeres ved å legge til linjen med kode under.

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

Denne koden kjører basert på hvilken verdi "name" har. Dette er en string som sendes av brukeren. Hvis den har verdien "middag" vil de tre linjene under kjøre.

```
case "middag":
     index = random.Next(mat.Count);
     return new OkObjectResult(mat[index]);
```

Den første linjen genererer en tilfeldig verdi fra 0 til mat.Count verdien. mat.Count verdien er antall elementer i listen mat. Fra eksempelet over vil denne verdien være 6.  
De andre casene vil gjøre det samme.
Hvis du har laget en egen liste må du lage en tilsvarende case for det.

Til slutt så legger vi til en default response. Fjern først den gamle "return OkObjectResult" og legg til denne linjen under helt til slutt (Husk å legge den utenfor krøllparentesene i switch-statementen):

```
return new OkObjectResult("Brukbare kommandoer er: middag, gjøre, mynt, pils");
```

Denne meldigen blir returnert når meldingen ikke inneholder noen verdi for "name". Oppdater den med dine nye kommandoer(switch cases) som du har laget!

## Send den til Azure Functions

- Lag en ny "FunctionApp" i Azure, som du gjorde i Microsoft-guiden tidligere.
- Gå til "Workspace" og klikk på "Azure functions" knappen. Det er knappen med Lyn inni to blå krokodilletegn.
- Velg Deploy to Function App.
- Velg den nye FunctionAppen du nettop lagde.
- Gå til resources, velg riktig FunctionApp og høyreklikk på klassen under mappen "Functions". Klikk på Execute function nå.
- Erstatt Azure med kommandoen du vil utføre, i pop-up boksen som kommer opp.

Du kan også kjøre den direkte i nettleser eller med Postman ved å gå den riktige URLen.  
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
Vil du legge til flere lister og kommandoer? Kanskje du heller vil bruke dette til å gjøre noe helt annet? Bare fantasien setter grenser.

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

# Having trouble making decisions?

Are you spending an unreasonable amount of time making small decisions that will have no effect on your future?
Then this small project might be for you! The small decisions could be choosing whats for dinner, what to drink tonight, or maybe just deciding on a 50/50 choice, where you would've flipped a coin, but who carries coins nowadays?

In this project you will make a list of possible outcomes in a choice, then the script will return a random decision.
This will be done by using Azure Functions which is always running in the "cloud", which means that it will always be available whenever you need to make a choice. 

## How to get started

###

This guide is written in C#, which is an object oriented programming language that looks quite similar to Java.
To run this locally, you need to download the .NET framework from here https://dotnet.microsoft.com/en-us/download

### Follow the guide in the link below
https://learn.microsoft.com/en-us/training/modules/develop-azure-functions/5-create-function-visual-studio-code
Note! If you encounter problems with VSCode not recognizing the Microsoft packages after installing them, try to close all instances of VSCode and then re-open it.
If the problem still persists, try this command in the terminal (Right click on the folder and select "Open in integrated terminal"):

```
dotnet restore --force-evaluate
```

Did you complete the guide? Then you can start with further developments!

## Extensions

Your code will look similar to this after following the guide above:

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
The first thing you need to do is remove this line:

```
string responseMessage = string.IsNullOrEmpty(name)
? "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."
: $"Hello, {name}. This HTTP triggered function executed successfully.";
```
Next is to create the lists with possible outcomes. You will need to make a list with different choices, and place it where you just removed the previous line of code. Lists in C# look like this:

```
var mat = new List<string>{ "Pizza","Taco","Pasta","Børek","Kebab","Brød"};
```
You probably need to import the list class. This is done by adding this line of code at the top of the file with the other "using" statements.

```
using System.Collections.Generic;
```
This is a list that is called "mat" and contains six "string" objects.
You can add and remove as many food dishes as you would like.
The list "mat" is meant for deciding what to have for dinner. If there are other choices you want to add, you just need to create more lists containing the different outcomes.
Here are some examplelists:

```
var mat = new List<string>{ "Pizza","Taco","Pasta","Børek","Kebab","Brød"};
var gjøre = new List<string>{ "Sove","Lese","Gå ut","Sove","Chille","Sove"};
var mynt  = new List<string>{ "Kron","Mynt"};
var pils = new List<string>{ "Ringnes","Schous", "Tuborg", "Frydenlund", "Carlsberg", "Aass", "Hansa", "Billigste", "Ny","Isbjørn"};
```
After creating the lists, we need a Random-object. This is the object that will return a random number, thus making the choice.
The random object is created like this:

```
var random = new Random();
```
This is an object that is part of C#'s "System" package, and thus needs to be imported by adding the line below, at the very top like the previous "Using" statement.

```
using System;
```
After this we need an index, which is an integer. Add following lines of code below where you created the random object.

```
int index = 0;
```
Now comes the part where the code will decide on a random outcome from each of the lists.

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
This code will run based on what value "name" has. This is a string that is sent by the user. If the value is "middag" the upper three lines will run.

```
case "middag":
     index = random.Next(mat.Count);
     return new OkObjectResult(mat[index]);
```
The first line generates a random number from 0 to mat.Count. mat.Count is the count of elements in the list "mat". With our example code above, this value will be 6.
The other cases does the same.
If you have made your own list, you need to make a "case" for it as well.

At the end we need to add a default response. Remove the old "return OkObjectResult" and replace it with it the line below. (Remember to put it outside the curly brackets in the switch-statement):
```
return new OkObjectResult("Brukbare kommandoer er: middag, gjøre, mynt, pils");
```
This message is returned when the user sent message doesn't have any value for "name". Update it with the new commands(switch cases) you've made!

## Upload it to Azure Functions

- Create a new "FunctionApp" in Azure, like you did in the Microsfot-guide earlier.
- Go to "Workspace" and click on the "Azure functions" button. Its the button with a lightning and two blue "greater-than" signs.
- Choose Deploy to Function App
- Choose the new FunctionApp you just created.
- Go to resources, choose the right FunctionApp and rightclick on the class in the folder "Functions". Click Execute function now.
- Replace Azure with the command you want to run, in the pop-up box that pops up.

You can also run it directly in the browser or with Postman by using the correct URL.
You can find yout URL by doing this:
- Go to portal.azure.com
- Click on Function App (Use the search field if you can't find it)
- Click on the FunctionApp name you made.
- Under Overview there will be a list of functions you've deployed, click on it.
- Click on the "Get function URL" button and copy the link.
- Paste it into your browser and add name and command at the end and click enter. See example below.

```
name=mynt
```

Normally the URL is formatted like this:

```
https://{NameOfYourFunctionApp}.azurewebsites.net/api/{NameOfYourFunction}?name={Command}
```
Replace the values in the curly brackets with your own.
**Note! To run the function on your phone, you need to use the URL.**

## Further developments
Now you can develop your function further, any way you like!
Want to add more lists and commands? Or maybe you want to do something completely different? Your creativity is the limit.

### Full code
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
