- OPG 1
    - 1A https://xizvytyy0i.execute-api.eu-west-1.amazonaws.com/Prod/hello
     - 1B https://github.com/GenjiPlayer/DevOpsEksamen2024/actions/runs/12015666454
        
    
- OPG 2
    - 2A 
   
     - 2B https://github.com/GenjiPlayer/DevOpsEksamen2024/actions/runs/12015666454/job/33494213133
          https://github.com/GenjiPlayer/DevOpsEksamen2024/actions/runs/11989339673/job/33425617990
     

- OPG 3
    - Fikk ikke til denne oppgaven
   
       
    

-    OPG4
    - Se terraform.tfvars og main.tf i infra mappen

  - OPG 5

 1. Automatisering og kontinuerlig levering (CI/CD)
Serverless-arkitektur lar utviklere kode og kjøre koden uten å trenge å tenke på å holde styr på egne servere og den underliggende infrastrukturen. Utviklere vil kun trenge å sende koden til en feks AWS sky-plattform, som vil behandle og kjøre koden ettersom plattformen er konfigurert. Applikasjoner som er bygget med mikrotjenester-arkitektur består av flere små selvstendige tjenester som kjører sin egen prosess.
Den serverless-arkitekturen sender små isolerte funksjoner. Dette gjør utrullingen rask og fleksibel. 
I Mikrotjenester kreves det et mer avansert oppsett for CI/CD. Det bygges containere og koordineres mellom tjenester. Dette er mer komplekst og gir en bedre kontroll over systemet enn det en serverless-arkitektur vil gi.

2. Observability (overvåkning) 
Det er større kontroll over logging og overvåkning i ved bruk av mikrotjenester ettersom det ofte blir kjørt som containere. Ettersom at funksjonene i serverless-arkitektur genererer mye distribuert data og er kortlevde, vil det være vanskeligere å holde følge med på hva som skjer i systemet. Det er vanskelig å følge en hel prosess som involverer flere funksjoner. 

3. Skalerbarhet og kostnadskontroll
I en mikrotjenestebasert arkitektur og en serverless en skaleres det automatisk når nye instanser av funksjoner startes. Fordelen i den serverless arkitekturen er at det ikke kreves å konfigurere infrastruktur for skalering, kontra mikrotjenester hvor det trengs.  
Kostnadene i mikrotjenester er forutsigbare ettersom at de er basert på servere eller containere. I den serverlesse arkitekturen er kostnadene basert på funksjonenes bruk. 

4. Eierskap og ansvar
Utviklerne med mikrotjeneste arkitekturen har fullt ansvar for infrastrukturen og alle tjenester. De er også ansvarlige for systemets ytelse og må derfor sikre at systemet er oppe og fungerer. Kostnadene kan forutses ut i fra infrastrukturen. Utviklerne vil derfor kunne jobbe for å minske kostnadene ved å bruke færrest mulig resurser. 
Hos den serverlesse arkitekturen vil utviklerne kun fokusere på koden og slippe å tenke på infrastrukturen, ettersom skyleverandøren tar seg av det. DevOps teamet vil følge med på hvordan det går med infrastrukturen, men de vil hovedsakelig fokusere på optimalisering av funksjoner. Kostnadene er basert på funksjonene som brukes og vil derfor kunne redusere kostnader.


