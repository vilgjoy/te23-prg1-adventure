

BOOK = [
    {
        "id": 1,
        "title": "Neonstadens Skuggor",
        "text": "Regnet smattrar mot asfalten i Neo-Tokyos undre värld. Du står utanför en liten verkstad där du ska möta en hackare som sägs ha information om det korrupta megaföretaget 'Zenith Corp'.",
        "options": [
            {"text": "Gå in i verkstaden.", "next_id": 2},
            {"text": "Avvakta och spana från skuggorna.", "next_id": 3},
        ],
    },
    {
        "id": 2,
        "title": "Hackarens Verkstad",
        "text": "Verkstaden är fylld med gamla skärmar, kablar och halvmonterade drönare. En figur med neonblå cyberögon vinkar dig närmare. 'Jag har det du behöver, men Zenith är oss på spåren'.",
        "loot": "Databricka med Zeniths hemligheter",
        "options": [
            {"text": "Ta emot databrickan och fly bakvägen.", "next_id": 4},
            {"text": "Fråga om mer information.", "next_id": 5},
            {"text": "Be om extra utrustning.", "next_id": 15},
        ],
    },
    {
        "id": 3,
        "title": "Skuggornas Trygghet",
        "text": "Du ser två Zenith-drönare cirkulera ovanför. Hackaren är i fara. Du har en sekund på dig att agera!",
        "options": [
            {"text": "Spring in i verkstaden och varna hackaren!", "next_id": 2},
            {"text": "Försök smyga runt byggnaden och hitta en bakväg.", "next_id": 6},
        ],
    },
    {
        "id": 4,
        "title": "Flykt genom Bakgränden",
        "text": "Du kastar dig ut genom bakdörren. Sirener hörs på avstånd. Ditt cyberförstärkta öga varnar för värmesensorer i gränden. Zeniths säkerhetsstyrka är på jakt efter dig!",
        "options": [
            {"text": "Göm dig i en container.", "next_id": 7},
            {"text": "Spring genom gränden och försök undvika sensorerna.", "next_id": 8},
        ],
    },
    {
        "id": 5,
        "title": "Mer Information",
        "text": "Hackaren ser sig oroligt omkring. 'Zenith har en krypterad server i stadens centrum. Om du kan använda den här databrickan där, kan vi få fram sanningen.'",
        "options": [
            {"text": "Acceptera uppdraget och ta databrickan.", "next_id": 4},
            {"text": "Tacka nej och lämna verkstaden.", "next_id": 9},
        ],
    },
    {
        "id": 6,
        "title": "Bakvägen In",
        "text": "Du smyger runt byggnaden och ser en låst dörr. Du kan försöka dyrka upp den om du har rätt verktyg.",
        "options": [
            {"text": "Använd ett dyrkverktyg (om du har ett).", "next_id": 10, "requires": "Dyrkverktyg"},
            {"text": "Försök forcera dörren.", "next_id": 11},
        ],
    },
    {
        "id": 7,
        "title": "Gömstället",
        "text": "Du kryper ner i en container. Zeniths patruller går förbi utan att märka dig. Efter en stund är faran över, och du kan smyga vidare.",
        "options": [
            {"text": "Smyg iväg mot en säker plats.", "next_id": 12},
        ],
    },
    {
        "id": 8,
        "title": "Sensornätet",
        "text": "Du springer genom gränden men värmesensorerna börjar larma. Zeniths drönare dyker upp från ovan!",
        "options": [
            {"text": "Försök springa snabbare och undvika drönarna.", "next_id": 13},
            {"text": "Slåss mot drönarna!", "next_id": 14},
        ],
    },
    {
        "id": 9,
        "title": "Omkring hörnen",
        "text": "Du går ut genom dörren och blir hittat av en Zenith-Drönare. Du tror du är ok, men eftersom Zenith-drönaren såg dig pratade med figuren, börjar den attackera!",
        "options": [
            {"text": "Slåss mot drönarna!", "next_id": 14},
            {"text": "Försök springa iväg och undivk drönaren.", "next_id": 13},
        ],
    },
    {
        "id": 10,
        "title": "Inne i Byggnaden",
        "text": "Dörren klickar upp tyst. Du smyger in och hittar ett övergivet laboratorium. På ett bord ligger ett gammalt EMP-granat, som kan vara användbart mot Zeniths drönare.",
        "loot": "EMP-granat",
        "options": [
            {"text": "Ta EMP-granaten och leta vidare.", "next_id": 16},
            {"text": "Lämna snabbt innan någon upptäcker dig.", "next_id": 12},
        ],
    },
    {
        "id": 12,
        "title": "",
        "text": "String text for page",
        "options": [
            {"text": "Option 1 with next page id", "next_id": 2},
            {"text": "Option 2 with next page id", "next_id": 3},
        ],
    },
    {
        "id": 13,
        "title": "Flykt från drönarna",
        "text": "Du ökar takten och försöker hitta en väg genom gränden för att undkomma drönarna. Du lyckas skugga dig bakom ett stort lastbilsliknande objekt och undviker en första radarpass. Du hör dock fortfarande drönarna surrande över dig.",
        "options": [
            {"text": "Smyg bort till en sidogata för att komma undan.", "next_id": 15},
            {"text": "Hoppas på att det finns någon som kan hjälpa dig här i gränden.", "next_id": 16},
        ],
    },
    {
        "id": 14,
        "title": "Äntligen klar...",
        "text": "Efter en svår strid, klarar du faran utan någon stor skada. Du tittar på Zenith-drönaren och hittar en ny vapenmodell som fortfarande fungerar - en Laser Rifle och några kreditchips. Banditer i närheten dock ser detta och dyker upp.",
        "loot": "Laser Rifle",
        "options": [
            {"text": "Fortsätt strida trots den minimala skadan skadan.", "next_id": 17},
            {"text": "Betala banditerna med chips (om du har det)", "next_id": 18, "requires": "Kreditchips"},
        ],
    },
    {
        "id": 15,
        "title": "Extra Utrustning",
        "text": "Hackaren rotar i en låda och slänger en liten enhet till dig. 'Här, ett dyrkverktyg. Kan komma till nytta.'",
        "loot": "Dyrkverktyg",
        "options": [
            {"text": "Tacka och gå bakvägen ut.", "next_id": 4},
            {"text": "Fråga om mer utrustning.", "next_id": 5},
        ],
    },
    {
        "id": 16,
        "title": "Dolda Sanningen",
        "text": "I laboratoriets hörn finner du en terminal. Den verkar innehålla information om Zeniths experiment. Om du har databrickan kan du ladda upp filerna.",
        "options": [
            {"text": "Ladda upp databrickan (om du har den).", "next_id": 17, "requires": "Databricka med Zeniths hemligheter"},
            {"text": "Lämna byggnaden och smyga iväg.", "next_id": 12},
        ],
    },
    {
        "id": 17,
        "title": "Banditernas Hot",
        "text": "Du lyfter vapnet och gör dig redo för strid. Banditerna ser din beslutsamhet men tvekar inte. En av dem drar en kniv medan en annan laddar ett gammalt hagelgevär. Striden är oundviklig.",
        "enemy": "Street-Bandits",
        "combat": True,
        "options": [
            {"text": "Attackera med ditt vapen!", "next_id": 19},
            {"text": "Försök skrämma dem med din närvaro.", "next_id": 20},
        ],
    },
    {
        "id": 18,
        "title": "Mutan går igenom",
        "text": "Du räcker över några kreditchips till banditerna. De granskar dem och nickar nöjt. 'Smart val,' säger en av dem innan de försvinner in i mörkret. Du kan nu fortsätta vidare utan strid.",
        "options": [
            {"text": "Smyg vidare genom gränden.", "next_id": 21},
            {"text": "Göm dig en stund för att se om de verkligen gått.", "next_id": 22},
        ],
    },
        {
        "id": 19,
        "title": "Efter Striden",
        "text": "Banditerna ligger besegrade på marken. En av dem lyckas stappla iväg, medan den andra stönar av smärta. Du genomsöker deras tillhörigheter och hittar några kreditchips och en skadad datapad med Zeniths logotyp.",
        "loot": ["Kreditchips", "Skadad Datapad"],
        "options": [
            {"text": "Ta datapaden och undersök den senare.", "next_id": 23},
            {"text": "Lämna platsen snabbt innan fler fiender dyker upp.", "next_id": 24},
        ],
    },
    {
        "id": 20,
        "title": "Banditerna Backar",
        "text": "Efter ditt hot ser banditledaren på dig en stund innan han fnyser och vänder sig om. 'Inte värt besväret', muttrar han. De försvinner in i skuggorna, och du står kvar med Zenith-drönarens trasiga skal vid dina fötter.",
        "options": [
            {"text": "Genomsök vraket för användbara delar.", "next_id": 25},
            {"text": "Lämna snabbt innan någon annan dyker upp.", "next_id": 26},
        ],
    },
    {
        "id": 21,
        "title": "Vidare i Natten",
        "text": "Med hotet undanröjt fortsätter du genom de smala bakgatorna. Neonljusen flimrar ovanför medan du smälter in i stadens skuggor. Du vet att Zeniths säkerhet snart kommer att patrullera området.",
        "options": [
            {"text": "Fortsätt mot stadens centrum.", "next_id": 27},
            {"text": "Försök hitta en säker plats att vila på.", "next_id": 28},
        ],
    },
    {
        "id": 22,
        "title": "Ett Sista Öga på dem",
        "text": "Du väntar i skuggorna och ser hur banditerna försvinner längre in i gränden. Plötsligt hör du röster bakom dig – en patrull från Zeniths säkerhetsteam är i närheten! Du måste agera snabbt.",
        "options": [
            {"text": "Försök smyga undan obemärkt.", "next_id": 29},
            {"text": "Leta efter en plats att gömma dig på.", "next_id": 30},
        ],
    }

]
