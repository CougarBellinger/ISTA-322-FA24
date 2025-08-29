>**Definition**: Building pipelines to make data useful for data scientists and analysts
#### Structured Data
- Fits into a database nicely
- ‘square’ or ‘cube’ formats
- Don’t need to do work to analyze or query
- ex: SQL DB with two tables -- No data processing needed to do this
#### Semi-Structured Data
- Has some consistent format
- Minimal work to get into useable format
- ex: JSON, XML, csv, tsv -- May take time, but relatively simple
#### Unstructured Data
- Text, pdf, images, video
- Zero structure
- Lots of work to extract useful data from
#### Note:
>Data engineers take the raw data that’s stored and coming in from all over the place and transform it to a useful format. Data scientists take this data and make inference from it.
#### Events
- Data of specific actions performed by entities
- Records time and who did it
- Linked to other data
#### Extract-Transform-Load (ETL)
- **Data Lake**: Stores raw data
- **Data Warehouse**: Stores transformed data
#### Big Data
- Utilize cluster of machines for data processing

![[WhatIsDE_DataAndTools.pptx.pdf]]