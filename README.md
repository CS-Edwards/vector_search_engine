# Weaviate Vector Database Project
Weaviate Overview and Semantic Search Demo

By: Candace Edwards
Email: [cedward2@hawaii.edu](mailto:cedward2@hawaii.edu)

This is the final project for ICS691B: Big Data Analytics, Fall 2022. Submitted: 12/15/22

In this project I’ve explored the relevant architecture of the Weaviate core node, implemented a vector database using Weaviate and applied three dimensionality reduction algorithms to provide 2D and 3D visualization of the vector data.

The data for this project is gathered by scraping the UH Manoa spring ‘23 registration page and course catalog page. Ultimately, we use course information such as the course name, course description, department and instructor to build our database objects and vectorize our data. 

## Deliverables
<ul>
<li> The final project note book is: `CEdwards_ICS691B_Final_Weaviate.ipynb`
<li> Python code for webscrape directory/file: `code/data_util.py`
<li> Data for dataframe directory/file: `data/data_df.csv`
<li> Vector embeddings numpy directory/file: `data/embeddings.npy`
</ul>


## Outline:

I. Project Overview <br>
II. Weaviate Overview<br>
----Architecture Overview<br>
----Vectors and Vector Index<br>
------kNN vs ANN<br>
------HNSW<br>
III. Vector Database Demonstration<br>
----Data and Vectors<br>
----Weaviate Database Instance<br>
----Semantic Search Queries<br>
IV. Visualizations<br>
----PCA<br>
----t-SNE<br>
----UMAP<br>
V. Conclusion<br>



### Misc:
Draft/Sandbox: `working_draft.ipynb`

