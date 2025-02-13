format = [
    {
        "id": 1,
        "title": "String title for page",
        "text": "String text for page",
        "options": [
            {"text": "Option 1 with next page id", "next_id": 2},
            {"text": "Option 2 with next page id", "next_id": 3},
        ],
    },
]

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
        "id": 16,
        "title": "Dolda Sanningen",
        "text": "I laboratoriets hörn finner du en terminal. Den verkar innehålla information om Zeniths experiment. Om du har databrickan kan du ladda upp filerna.",
        "options": [
            {"text": "Ladda upp databrickan (om du har den).", "next_id": 17, "requires": "Databricka med Zeniths hemligheter"},
            {"text": "Lämna byggnaden och smyga iväg.", "next_id": 12},
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
]
