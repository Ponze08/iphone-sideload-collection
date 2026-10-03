# Verifica della raccolta

Verificata il 3 ottobre 2026:

- Catalogo completo: 11 progetti, 10 link IPA e 1 percorso manuale per Amethyst.
- Tutti i 10 link IPA hanno risposto HTTP 200. Dimensioni confrontate con gli header HTTP.
- Scaricati realmente e verificati DolphiniOS, Clip e uYouEnhanced: struttura IPA e integrità ZIP corrette; SHA-256 DolphiniOS corrispondente al valore upstream.
- Corretto il valore di dimensione uYouEnhanced: la fonte dichiarava 118022104 byte, il file corrente è di 135840058 byte. Il valore originale è conservato nel catalogo.
- Verificato il riuso di un download già valido e il passaggio manuale Amethyst.
- Controlli di integrità: rifiutati file HTML, dimensione errata e hash errato.
- Script Python compilato correttamente.

Non eseguiti: installazione, firma, avvio su iPhone, configurazione JIT e funzionamento delle app dentro LiveContainer. Il launcher Windows non è stato eseguito in questo ambiente Linux. Le verifiche dei link descrivono lo stato alla data indicata.
