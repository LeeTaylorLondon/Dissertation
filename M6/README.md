## /M6/ File Structure

* **books_xml**  
This contains the book files as .xml files where each sentence is marked.  

 
* **data_prep**  
This contains .pkl files storing sentences extracted from the books stored in 'books_xml'. 
An object storing the set of unique words is also stored as a .pkl file. Lastly, a .py file
to create, store and load all of these objects is also stored here.


* **model_weights**  
The files stored here contain weights for different Word2Vec models.  

 
 
* **output_set_expansion**  
This folder contains output generated in attempt to recreate set expansion.  

  
* **scrapings**  
Each word from 'data_prep/entity_set.txt' is used in a google search for it's wikipedia page,
the text from the wikipedia is scraped and stored here in various files. 

 