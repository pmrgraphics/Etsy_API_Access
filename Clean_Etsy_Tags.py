# importing pandas as pd
import pandas as pd
import log

# Making data frame from the csv file
df = pd.read_csv('oldCoinCufflinks.csv')

column_to_replace = ("tags",
                     "materials",
                     "style",
                     )
# TODO Store still in JSON File?
data = {"[": "",
        "',": ",",
        ", '": ", ",
        "]": "",
        "'": ""
        }


@log.log_error()
def replace(column_to_replace, replace_from, replace_to):
    df[column_to_replace] = df[column_to_replace].str.replace(replace_from, replace_to, regex=True)

    return df


for column in column_to_replace:
    # next loop for dictionary here
    for x, y in data.items():
        replace_from = x
        replace_to = y
        replace(column, replace_from, replace_to)


output = df.to_csv("oldCoinCufflinks_clean.csv")
