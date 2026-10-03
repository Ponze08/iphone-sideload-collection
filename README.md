# iPhone Sideload Collection

Raccolta di 11 app per iPhone, con link ufficiali, download in blocco e guida di installazione. Preparata per Ponze08.

**La repo contiene il catalogo e lo scaricatore. Gli IPA vengono scaricati dagli autori sul tuo PC; non sono archiviati o ripubblicati qui.**

## Download rapido su Windows

Installa [Python 3.9+](https://www.python.org/downloads/windows/), scarica lo ZIP della repo, estrailo e apri `Scarica-tutte.cmd`. Lo script scarica 10 IPA disponibili. Amethyst resta un passaggio manuale.

Per vedere il catalogo o verificare i link:

```powershell
py -3 download_apps.py --list
py -3 download_apps.py --check
```

## Catalogo

| App | Versione selezionata | Download / progetto | Installazione |
| --- | --- | --- | --- |
| SideStore | 0.6.4 | [IPA ufficiale](https://github.com/SideStore/SideStore/releases/download/0.6.4/SideStore.ipa) · [Progetto](https://github.com/SideStore/SideStore) | SideStore: seguire la guida ufficiale |
| LiveContainer + SideStore | 3.8.0 | [IPA ufficiale](https://github.com/LiveContainer/LiveContainer/releases/download/3.8.0/LiveContainer%2BSideStore.ipa) · [Progetto](https://github.com/LiveContainer/LiveContainer) | iloader o Impactor |
| DolphiniOS | v5.0.0b6 | [IPA ufficiale](https://github.com/OatmealDome/dolphin-ios/releases/download/v5.0.0b6/Non-Jailbroken.ipa) · [Progetto](https://github.com/OatmealDome/dolphin-ios) | SideStore / AltStore Classic |
| Amethyst | Actions / compilazione | [Progetto](https://github.com/AngelAuraMC/Amethyst-iOS) | AltStore / SideStore |
| UTM SE | v4.7.5 | [IPA ufficiale](https://github.com/utmapp/UTM/releases/download/v4.7.5/UTM-SE.ipa) · [Progetto](https://github.com/utmapp/UTM) | App Store oppure sideload ordinario |
| Provenance | 3.3.0 | [IPA ufficiale](https://github.com/Provenance-Emu/Provenance/releases/download/3.3.0/Provenance-3.3.0-iOS.ipa) · [Progetto](https://github.com/Provenance-Emu/Provenance) | Sideload ordinario / app ufficiale |
| MAME4iOS | 2022.5 | [IPA ufficiale](https://github.com/yoshisuga/MAME4iOS/releases/download/2022.5/MAME4iOS-2022.5-250.ipa) · [Progetto](https://github.com/yoshisuga/MAME4iOS) | Sideload ordinario |
| iTorrent | v2.2.0-1 | [IPA ufficiale](https://github.com/XITRIX/iTorrent/releases/download/v2.2.0-1/iTorrent.ipa) · [Progetto](https://github.com/XITRIX/iTorrent) | Sideload ordinario |
| Clip | 1.2 | [IPA ufficiale](https://cdn.altstore.io/file/altstore/apps/clip/1_2.ipa) · [Progetto](https://github.com/rileytestut/Clip) | AltStore / SideStore, installazione diretta |
| uYouEnhanced | 21.14.4 | [IPA ufficiale](https://archive.org/download/YouTubeRebornPlus_19.10.5-4.2.6/yt-uYE-21144-305.ipa) · [Progetto](https://github.com/arichornlover/uYouEnhanced) | Sideload ordinario |
| Apollo Reborn | v1.15.11_3.8.5 | [IPA ufficiale](https://github.com/Apollo-Reborn/Apollo-Reborn/releases/download/v1.15.11_3.8.5/Apollo-Reborn-3.8.5-NOEXTENSIONS.ipa) · [Progetto](https://github.com/Apollo-Reborn/Apollo-Reborn) | Sideload ordinario |

## Installazione

Leggi [INSTALLAZIONE.md](INSTALLAZIONE.md) per il percorso LiveContainer + SideStore, l’installazione diretta e i requisiti delle singole app.

Scaricare un IPA non lo installa: firma, autorizzazioni Apple, pairing, JIT e login delle app vanno completati sul PC e sull’iPhone. Non è garantito che ogni app funzioni dentro LiveContainer o su ogni versione iOS.

LiveContainer richiede il proprio metodo di installazione: **non usare Sideloadly per LiveContainer**. La raccolta include la variante con SideStore integrato.

## Versioni e integrità

Catalogo verificato il 3 ottobre 2026. I link sono fissati a versioni specifiche: non viene selezionata automaticamente una nuova release o un fork. La beta DolphiniOS è indicata esplicitamente. SideStore usa 0.6.4 stabile.

Il downloader controlla dimensione, struttura IPA, integrità ZIP e SHA-256 quando pubblicato dall’autore. Scrive un resoconto locale in `downloads/download-report.json` e continua dopo il fallimento di un singolo download.

Per aggiornare una voce, controlla la fonte ufficiale e aggiorna `apps.json`. Alcuni link esterni o artifact possono diventare indisponibili.

## Crediti

Ogni app appartiene ai rispettivi sviluppatori. La licenza MIT di questa repo riguarda esclusivamente lo scaricatore e la documentazione originale. Non sono inclusi giochi, BIOS, certificati o credenziali.
