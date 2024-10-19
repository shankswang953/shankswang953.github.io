
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top. 
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd


# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:

publications = pd.read_csv("publications.tsv", sep="\t", header=0)
publications


# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:

import pandas as pd
import os

publications = pd.read_csv("publications.tsv", sep="\t", header=0)

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    return "".join(html_escape_table.get(c,c) for c in text)


for row, item in publications.iterrows():
    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    html_filename = str(item.pub_date) + "-" + item.url_slug
    year = item.pub_date[:4]
    
    md = "---\n"
    md += f"title: \"{item.title}\"\n"
    md += "collection: publications\n"
    md += f"permalink: /publication/{html_filename}\n"
    md += f"date: {str(item.pub_date)}\n"
    md += f"venue: '{html_escape(item.venue)}'\n"
    md += f"citation: '{html_escape(item.citation)}'\n"
    md += f"status: '{item.status}'\n"
    md += f"venue: '{html_escape(item.venue)}'\n"
    if item.status == 'prepare':
        md += f"collaborators: '{item.collaborators}'\n"
    
    if len(str(item.paper_url)) > 5:
        md += f"paperurl: '{item.paper_url}'\n"
    md += f"{index}. "  # Add the index number
    md += "---\n\n"
    if item.status == 'published':
    if item.status == 'published':
        md += f"Published in {item.venue}, {item.pub_date[:4]}\n\n"
    elif item.status == 'reviewing':
        md += "[under review]\n\n"
    elif item.status == 'prepare':
        md += f"Joint work with {item.collaborators}\n\n"
        md += f"Joint work with {item.collaborators}\n\n"
    if item.status == 'published':
        md += f"Recommended citation: {item.citation}"
        md += f"Recommended citation: {item.citation}"
    with open(f"../_publications/{md_filename}", 'w') as f:
        f.write(md)
        f.write(md)
    
    with open(f"../_publications/{md_filename}", 'w') as f:
        f.write(md)