# Changelog

Tutte le modifiche a PDF Tool, dalla più recente.
Tipi di modifica: **Nuovo**, **Migliorato**, **Correzione**.

## [1.5.0] – 2026-09-23

### Nuovo
- **Divisione grafica**: il pulsante "Dividi" apre una modalità in cui si clicca sulle **forbici tra una pagina e l'altra** per scegliere i punti di taglio. Ogni gruppo prende un colore e ha sopra un campo per il **nome del file**. In questa modalità il trascinamento delle pagine è disattivato. Restano i pulsanti "Taglia tutte" (un file per pagina) e "Rimuovi tagli". Sostituisce la vecchia finestra con gli intervalli scritti a mano.
- **Opzioni di salvataggio**: qualità *Originale* (predefinita), *Alta* 200 dpi, *Media* 150 dpi, *Bassa* 100 dpi, e **bianco e nero**. Qualità ridotta e bianco e nero trasformano ogni pagina in un'immagine: un avviso spiega che si perdono testo selezionabile, ricerca e OCR e che il peso può anche aumentare per i PDF di solo testo. Con il bianco e nero anche timbri e testo inseriti diventano grigi.
- **Cursore per la dimensione delle miniature**, che vengono ridisegnate più nitide quando le ingrandisci. La dimensione scelta viene ricordata.

### Migliorato
- A salvataggio finito viene indicato il peso del file ottenuto.

## [1.4.0] – 2026-09-23

### Nuovo
- **Timbri**: immagini PNG (anche con sfondo trasparente) o JPG da sovrapporre alle pagine, con spostamento e ridimensionamento nell'anteprima. Si possono applicare in un colpo solo a tutte le pagine selezionate.
- I timbri restano **salvati in questo browser**, solo su questo computer, e sono pronti al prossimo avvio. Con **Esporta/Importa** si crea un file di backup da conservare o portare su un altro PC.
- **Testo**: blocchi di testo su più righe con carattere (Helvetica, Times, Courier), grassetto, corsivo, dimensione, colore, allineamento e opacità. Nel PDF resta **vero testo**, selezionabile e ricercabile.
- Timbri e testo non rasterizzano la pagina: il contenuto originale resta intatto (a meno che la pagina non sia anche censurata).

### Migliorato
- I PDF vengono elaborati in un processo in background anche aprendo il programma con un doppio clic: l'interfaccia non si blocca più con i file grandi.

## [1.3.0] – 2026-09-22

### Nuovo
- **Censura** di parti della pagina. Nell'anteprima ingrandita, o dal pulsante sulla miniatura, si attiva la modalità censura (tasto `C`) e si trascina per disegnare rettangoli neri. Si possono spostare, ridimensionare ed eliminare, e Ctrl+Z annulla.
- **Censura sicura**: al salvataggio ogni pagina censurata viene trasformata in immagine a 200 dpi con i rettangoli neri già dipinti. Sotto il nero non resta nulla: né testo, né OCR, né immagini.

### Migliorato
- Avvisi chiari prima di salvare: le pagine censurate **perdono testo selezionabile, ricerca e OCR**, e i dati coperti **non sono recuperabili**.
- I file che contengono censure ricevono il suffisso `_censurato`. Se il nome scelto coincide con quello di un file aperto, c'è un avviso che si rischia di sostituire l'originale.

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
