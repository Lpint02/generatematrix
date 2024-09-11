# Generatore di Matrici Diagonalmente Dominanti

Questo script Python genera una matrice diagonalmente dominante di dimensione n x n e un vettore dei termini noti b, salvandoli in un file di testo con un formato specifico.

### Funzionalità principali

**Generazione di Matrice Diagonalmente Dominante**: La matrice A viene generata con elementi casuali compresi tra -5 e 5, con densità personalizzabile (di default il 20% degli elementi è diverso da zero). Viene garantito che la matrice sia diagonalmente dominante aggiungendo un fattore alla diagonale principale.

**Generazione del Vettore dei Termini Noti**: Viene creato un vettore b di dimensione n con valori casuali compresi tra 0 e 1.

**Salvataggio su File**: La matrice A e il vettore b vengono salvati in un file di testo con il seguente formato:
    Gli elementi della matrice sono separati da virgole, e le righe della matrice sono separate da punti e virgola (;).
    Il vettore b viene separato dalla matrice da una linea contenente tre trattini (---).
    Gli elementi del vettore b sono separati da virgole.
    Il file viene salvato con un timestamp nel nome per evitare sovrascritture.

### Requisiti
  Python 3.x
  
  Librerie:numpy
  
### Installazione delle dipendenze
  Assicurati di avere installato numpy. Se non lo hai installato, puoi farlo usando pip:
                                        
    pip install numpy

### Esecuzione dello script

**Parametri Principali**:

- `n`: dimensione della matrice e del vettore (n x n per la matrice e n per il vettore).  
- `factor`: fattore moltiplicativo utilizzato per rendere la matrice diagonalmente dominante.  
- `folder_path`: percorso in cui verrà salvato il file di testo.

**Modifica del percorso di salvataggio**:  
Specifica il percorso della cartella dove vuoi salvare i file aggiornando la variabile `folder_path`.

**Esecuzione dello script**:  
Lo script può essere eseguito direttamente da terminale o da un IDE Python. Ad esempio:
                                    
    python generate_matrix.py
    
### Note aggiuntive
  Assicurati che il percorso specificato in folder_path sia valido. Se la cartella non esiste, lo script la creerà automaticamente.
  La dimensione massima del file non deve superare 125 MB.
  
    
  





  


