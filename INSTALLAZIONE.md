# Installazione su iPhone

Il pacchetto raccoglie 11 progetti. Lo script scarica gli IPA disponibili, ma non collega il telefono, non firma app, non inserisce credenziali Apple e non abilita JIT. La compatibilità effettiva va verificata sul dispositivo con la sua versione esatta di iOS.

## 1. Scaricare gli IPA su Windows

Installa [Python 3.9 o superiore](https://www.python.org/downloads/windows/) con l'opzione **Add Python to PATH**, estrai lo ZIP e fai doppio clic su `Scarica-tutte.cmd`. Gli IPA vengono salvati in `downloads/<nome-app>/`. Il download completo richiede circa 1,7 GB; Provenance da solo supera 1 GB. Amethyst richiede il passaggio manuale descritto sotto.

Puoi anche scaricare una singola app:

```powershell
py -3 download_apps.py --app itorrent
```

Oppure selezionarne più di una:

```powershell
py -3 download_apps.py --app clip --app apollo
```

Le versioni sono fissate nel catalogo per rendere riproducibile la raccolta. Per aggiornare un'app, verifica la sua pagina ufficiale e aggiorna i metadati in `apps.json`.

## 2. Configurare LiveContainer + SideStore

Per gestire più app con account gratuito, parti dalla [guida ufficiale LiveContainer + SideStore](https://livecontainer.github.io/docs/installation/lc_sidestore). La release della raccolta contiene SideStore integrato: non è necessario installare anche SideStore standalone.

1. Scarica `LiveContainer+SideStore.ipa` dal catalogo.
2. Segui la guida ufficiale per installarlo tramite **iloader** o **Impactor**, usando il PC e l'iPhone collegato.
3. Completa i passaggi di pairing e VPN indicati nella guida.
4. Configura la firma senza JIT e verifica il risultato dalla pagina diagnostica JIT-less di LiveContainer.
5. Trasferisci gli altri IPA in File sull'iPhone. In LiveContainer premi `+` e importa quelli che vuoi provare.

**Sideloadly non è supportato per installare LiveContainer.** Per la variante standalone, la release 3.8.0 richiede SideStore 0.6.2+ oppure AltStore 2.2.1+.

Le app importate sono eseguite dentro LiveContainer. Non tutte funzionano: controlla la [lista ufficiale di compatibilità](https://github.com/LiveContainer/LiveContainer/wiki/App-Compatibility). Estensioni, tastiere e attività in background possono richiedere l'installazione diretta; per esempio Clip va preferibilmente installato direttamente tramite AltStore/SideStore.

## 3. Installazione diretta con Sideloadly

Per gli IPA ordinari che lo supportano, usa [Sideloadly ufficiale](https://sideloadly.io/):

1. Installa i componenti Apple per Windows indicati dal sito Sideloadly.
2. Collega e sblocca l'iPhone, poi autorizza il computer.
3. Carica un IPA e inserisci l'Apple Account nel programma.
4. Avvia la firma e conferma il codice Apple quando richiesto.
5. Autorizza il profilo da **Impostazioni → Generali → VPN e gestione dispositivo**.
6. Se richiesto, abilita **Impostazioni → Privacy e sicurezza → Modalità sviluppatore**, riavvia e conferma.

Con un account gratuito le app firmate normalmente scadono dopo 7 giorni e il limite ordinario è 3 app attive, incluso lo store usato per firmarle. Non puoi quindi installare direttamente tutte le app contemporaneamente con quel metodo. LiveContainer offre un'altra modalità di esecuzione, soggetta alla compatibilità delle singole app.

## 4. Passaggi specifici

| App | Passaggio ulteriore |
| --- | --- |
| SideStore | Segui [la documentazione ufficiale](https://docs.sidestore.io/); il solo IPA non completa pairing, VPN e refresh. La raccolta seleziona 0.6.4 stabile anziché 0.7.0-alpha. |
| LiveContainer | Usa il metodo sopra. La variante integrata contiene anche SideStore. |
| DolphiniOS | La raccolta include la beta ufficiale 5.0.0b6 non-jailbroken. Segui [le istruzioni ufficiali](https://dolphinios.oatmealdome.me/beta) per configurare JIT; installare l'IPA da solo non lo abilita. Aggiungi i tuoi giochi separatamente. |
| Amethyst | Non ci sono release IPA nel progetto originale. Cerca un artifact IPA disponibile nella [pagina Actions ufficiale](https://github.com/AngelAuraMC/Amethyst-iOS/actions); GitHub può richiedere login e gli artifact possono scadere. Se non disponibile, segui la compilazione ufficiale. Richiede JIT e un account Minecraft Java. Il supporto alla tua versione esatta di iOS deve essere verificato. |
| UTM | È selezionato **UTM SE**, che funziona senza JIT. Per la variante completa con JIT usa [la guida UTM](https://docs.getutm.app/installation/ios/). Importa un sistema operativo separatamente. |
| Provenance | Importa i tuoi giochi e gli eventuali BIOS. I requisiti JIT dipendono dal sistema emulato e dal core. |
| MAME4iOS | È selezionata la build iOS 2022.5 con core 0.250. Usa ROM compatibili con quel core. |
| iTorrent | Importa magnet o torrent dall'app; i download in background restano soggetti alla gestione iOS. |
| Clip | IPA 1.2 dalla fonte AltStore ufficiale. Configura i permessi e la tastiera dall'app, preferibilmente installata direttamente. |
| uYouEnhanced | Il progetto originale non ospita IPA nelle release GitHub. Il catalogo usa il link pubblicato nella fonte ufficiale dell'autore; il file resta sul servizio esterno scelto dall'autore. In alternativa segui [la guida di compilazione](https://github.com/arichornlover/uYouEnhanced/wiki/Building). |
| Apollo Reborn | È selezionata la variante senza estensioni per ridurre gli App ID. Configura il login secondo [le istruzioni ufficiali](https://apolloreborn.app/). |

Gli IPA vengono scaricati dai rispettivi autori o dai link delle loro fonti ufficiali. Questa raccolta non contiene giochi, BIOS, account o certificati personali. I checksum verificano l'integrità del file; non costituiscono una revisione del suo codice.
