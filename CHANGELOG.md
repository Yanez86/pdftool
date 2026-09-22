# Changelog

Tutte le modifiche a PDF Tool, dalla più recente.
Tipi di modifica: **Nuovo**, **Migliorato**, **Correzione**.

## [1.2.0] – 2026-09-22

### Nuovo
- Apertura dei **PDF protetti da password**: il programma chiede la password e, se è sbagliata, permette di riprovare.
- **Protezione con password** dei PDF salvati, con cifratura AES a 256 bit, dal pulsante con il lucchetto. Vale per Salva, Estrai selezione e Dividi. La password non viene memorizzata da nessuna parte.
- Se apri un PDF protetto, i file salvati mantengono la stessa password. Si può cambiare o togliere dal lucchetto.
- Apertura dei file firmati digitalmente **.p7m**, anche con firme multiple (`.p7m.p7m`) e in formato testo (Base64). Il PDF contenuto viene estratto e vengono mostrati nome del firmatario e data della firma, letti dal file e **non verificati**. Il PDF salvato è una copia senza firma digitale.
- Per le fatture elettroniche `.xml.p7m` si può scaricare il file XML estratto.

## [1.1.0] – 2026-09-22

### Nuovo
- Si possono aggiungere foto **JPG e PNG** come pagine. Ogni foto diventa una pagina A4, verticale o orizzontale in base alla foto, e si può ruotare, spostare ed eliminare come le altre pagine.
- Le foto scattate col telefono vengono raddrizzate automaticamente (orientamento EXIF).
- Finestra **Novità** con l'elenco delle modifiche: si apre dal pulsante con la versione in basso a destra.
- Barra in fondo con la firma "made by TheRealGibo".

## [1.0.1] – 2026-09-21

### Correzione
- Risolto l'errore "Expected instance of e, but got instance of undefined" che compariva salvando PDF cifrati: bollette, estratti conto, documenti firmati.

### Migliorato
- Se un PDF non si riesce a leggere, il programma ne ricava una copia pulita, sempre in locale, e riprova.

## [1.0.0] – 2026-09-21

### Nuovo
- Prima versione: elimina, ruota e riordina pagine, unisci più PDF, dividi un PDF (per pagina, ogni N pagine, per intervalli, per file di origine), estrai la selezione, rinomina i file salvati.
- Anteprima ingrandita, annulla (Ctrl+Z), tema chiaro e scuro automatico, funzionamento 100% offline.
