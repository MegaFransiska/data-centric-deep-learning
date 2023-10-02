## How I generate the chatgpt-annotation?

The objective of post generation by chatgpt is to build topic classification dataset. So I directly input a prompt to chatgpt to create text classification dataset with the given defined labels, and specifically generate the examples in csv format, so chatgpt will return the output in csv format as well.

PROMPT:

"""
Generate 90 text classification dataset with labels: {science, politics, sports} in csv format. Dataset contains single statement from news, following format the Dataset Samples:

Example:
post,topic
The athlete won a gold medal at the Olympics.,sports
The legislation was passed after a long debate in the Senate.,politics
The discovery of the Higgs boson at CERN marked a milestone in particle physics.,science
The swimmer broke the world record in the 100-meter freestyle.,sports
The bill received bipartisan support and was signed into law by the president.,politics
The recent findings on black holes have revolutionized our understanding of space-time.,science
The spacecraft successfully docked with the International Space Station.,science
The gymnast captured the audience's hearts and took home the bronze medal.,sports
"After months of negotiations, the climate accord was finally agreed upon by the majority of nations.",politics
"Scientists successfully cloned a sheep, sparking ethical debates worldwide.",science
"""
