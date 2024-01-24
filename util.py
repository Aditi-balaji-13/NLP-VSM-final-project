# Add your import statements here



import numpy as np


# Add any utility functions here
import nltk
nltk.download('omw-1.4')
def split(txt, seps):
    default_sep = seps[0]

    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]
