Anteckningar till inspelning: https://youtu.be/DAqJD1hBzZw


# Agenda för testning

- Från krav till testfall

Krav:

**Kontorsmätaren**

Vi har flera kollegor som brukar klaga på temperaturen. Det finns dessutom värmefläktar på vissa kontor.

(krav är abstrakta och generella  ...)

## Krav

- K1: Som kontorsarbetare vill jag kunna avläsa temperaturen på kontoret.
- K2: Som kontorsarbetare vill jag se om det är tänt på kontoret.

---

Utforskande testning.

Kör igång applikationen. Funderar kring hur användaren har det.

- Vi har startat applikationen.
- Vi har kopplat in USB-kabel till datorn.
- Vi har startat Atom.io.
- Vi kan se temperatur i konsol. Men även andra saker.

Tidigt system / implementation -> 
Är detta vad kunden vill ha?

Kundens feedback:
- Daggpunkt och luftfuktighet. Ej intressant.
- Kunden gillar att visa data i konsol. 

Nästa åtgärd: Skriv ett manuellt testfall

- Vad är det vi ska testa?
    - Kontorsmätarenheten

### Vad behöver vi göra för att kunna testa?

| Namn | Prereq | Input | Beteende | Resultat |
| ---  | ---    | ---   | ---      | ---      |
| K1.1 Mät temperatur | Pymakr | Atom, USB-kabel | "Temperaturen i kontoret är 23 °C" | Pass |
| K1.2 Temperatur ändras | K1.1 | Observera temp, värm upp 20s | Förhöjd temperatur | Pass |
| K2.1 Det är tänt | K1.1 | Tänd lampan i kontoret | "Lampa tänd" | Fail |


