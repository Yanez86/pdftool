# PDF Tool

Editor PDF leggero che gira **interamente nel browser**, in un unico file HTML.
Non installa nulla, non ha bisogno di internet e **nessun dato lascia il tuo computer**.

## Cosa fa

- **Elimina pagine**: una alla volta o selezionandone più di una
- **Ruota** singole pagine (90° a sinistra o a destra)
- **Riordina** le pagine trascinandole
- **Unisce** più PDF: aggiungi i file e salvali come un unico documento
- **Divide** un PDF: una pagina per file, ogni N pagine, per intervalli (`1-3, 4-7, 8-`) o per file di origine
- **Estrae** le pagine selezionate in un nuovo PDF
- **Rinomina** i file prima di salvarli, anche ogni singola parte quando dividi
- **Foto come pagine**: aggiungi immagini JPG o PNG, ognuna diventa una pagina A4 ruotabile
- Anteprima ingrandita, annulla (Ctrl+Z), tema chiaro e scuro automatico

## Come si usa

1. Scarica `index.html` (puoi rinominarlo come vuoi, ad es. `PDF Tool.html`)
2. Aprilo con un doppio clic: si apre nel browser
3. Trascina nella finestra i PDF o le foto

Funziona con Chrome, Edge, Firefox e Safari recenti. Con **Chrome ed Edge** si apre la
finestra "Salva con nome" e, quando dividi, puoi salvare tutte le parti direttamente in una cartella.
Con gli altri browser i file finiscono nella cartella Download.

### Scorciatoie

| Tasto | Azione |
|---|---|
| Clic / Maiusc+clic | Seleziona una pagina / un intervallo |
| Doppio clic | Anteprima ingrandita (← → per scorrere) |
| `Canc` | Elimina le pagine selezionate |
| `R` / `Maiusc+R` | Ruota a destra / a sinistra |
| `Ctrl+A` | Seleziona tutto |
| `Ctrl+Z` | Annulla |
| `Ctrl+S` | Salva |
| `Ctrl+O` | Aggiungi PDF |

## Privacy

- Le librerie (pdf-lib e pdf.js) sono **incorporate** nel file: non si scarica niente da CDN.
- Una Content-Security-Policy (`default-src 'none'`) impedisce alla pagina qualsiasi
  connessione di rete. Nel worker di pdf.js anche `fetch` è disattivato.
- Verifica: apri gli strumenti per sviluppatori (F12), scheda **Rete**, e usa il programma.
  Non comparirà nessuna richiesta.

## Come funziona

Il salvataggio usa **pdf-lib**, che copia le pagine così come sono. Testo, immagini, link e
qualità restano invariati e il testo resta selezionabile: non c'è nessuna conversione in immagine.
La rotazione modifica solo l'attributo `/Rotate` della pagina. Le miniature le disegna **pdf.js**.

I PDF cifrati senza password di apertura (bollette, estratti conto, documenti firmati) vengono decifrati in locale tramite pdf.js prima del salvataggio.

**Limiti:** i PDF protetti da password di apertura non si possono aprire. Moduli compilabili
e segnalibri (indice laterale) potrebbero non essere mantenuti dopo unione o divisione.

## Sviluppo

Il sorgente è `src/app.html`. `index.html` è generato e contiene le librerie incorporate:

```bash
npm install          # scarica pdf-lib e pdfjs-dist
python3 build.py     # rigenera index.html (~2,7 MB)
```

Per pubblicarlo online con **GitHub Pages**: *Settings → Pages → Deploy from branch → main / root*.
Anche da lì tutto resta elaborato in locale nel browser di chi lo usa.

## Novità

L'elenco delle modifiche è in [`CHANGELOG.md`](CHANGELOG.md) e nel programma, dal pulsante con il numero di versione in basso a destra.
Quando esce una nuova versione, la voce va aggiunta sia in `CHANGELOG.md` sia nella lista `CHANGELOG` all'inizio del codice in `src/app.html`.

## Licenza

MIT, vedi `LICENSE`. Le librerie incorporate hanno le loro licenze, vedi `THIRD_PARTY_LICENSES.md`.
