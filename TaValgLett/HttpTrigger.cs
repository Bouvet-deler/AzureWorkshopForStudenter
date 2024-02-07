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
