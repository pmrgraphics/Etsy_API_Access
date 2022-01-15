# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv('Amazon Upload December 2021.csv')

column_to_replace = (
                     "bullet_point1",

                     "bullet_point10",

                     )
# TODO Store This in JSON File?
data = {"109th": "110th",
        "108th": "109th",
        "107th": "108th",
        "106th": "107th",
        "105th": "106th",
        "104th": "105th",
        "103rd": "104th",
        "102nd": "103rd",
        "101st": "102nd",
        "100th": "101st",
        "99th": "100th",
        "98th": "99th",
        "97th": "98th",
        "96th": "97th",
        "95th": "96th",
        "94th": "95th",
        "93rd": "94th",
        "92nd": "93rd",
        "91st": "92nd",
        "90th": "91st",
        "89th": "90th",
        "88th": "89th",
        "87th": "88th",
        "86th": "87th",
        "85th": "86th",
        "84th": "85th",
        "83rd": "84th",
        "82nd": "83rd",
        "81st": "82nd",
        "80th": "81st",
        "79th": "80th",
        "78th": "79th",
        "77th": "78th",
        "76th": "77th",
        "75th": "76th",
        "74th": "75th",
        "73rd": "74th",
        "72nd": "73rd",
        "71st": "72nd",
        "70th": "71st",
        "69th": "70th",
        "68th": "69th",
        "67th": "68th",
        "66th": "67th",
        "65th": "66th",
        "64th": "65th",
        "63rd": "64th",
        "62nd": "63rd",
        "61st": "62nd",
        "60th": "61st",
        "59th": "60th",
        "58th": "59th",
        "57th": "58th",
        "56th": "57th",
        "55th": "56th",
        "54th": "55th",
        "53rd": "54th",
        "52nd": "53rd",
        "51st": "52nd",
        "50th": "51st",
        "49th": "50th",
        "48th": "49th",
        "47th": "48th",
        "46th": "47th",
        "45th": "46th",
        "44th": "45th",
        "43rd": "44th",
        "42nd": "43rd",
        "41st": "42nd",
        "40th": "41st",
        "39th": "40th",
        "38th": "39th",
        "37th": "38th",
        "36th": "37th",
        "35th": "36th",
        "34th": "35th",
        "33rd": "34th",
        "32nd": "33rd",
        "31st": "32nd",
        "30th": "31st",
        "29th": "30th",
        "28th": "29th",
        "27th": "28th",
        "26th": "27th",
        "25th": "26th",
        "24th": "25th",
        "23rd": "24th",
        "22nd": "23rd",
        "21st": "22nd",
        "20th": "21st",
        "19th": "20th",
        "18th": "19th",
        "17th": "18th",
        " 16th": " 17th",
        " 15th": " 16th",
        " 14th": " 15th",
        " 13th": " 14th",
        " 12th": " 13th",
        " 11th": " 12th",
        " 10th": " 11th",
        " 9th": " 10th",
        " 8th": " 9th",
        " 7th": " 8th",
        " 6th": " 7th",
        " 5th": " 6th",
        " 4th": " 5th",
        " 3rd": " 4th",
        " 2nd": " 3rd",
        " 1st": " 2nd",
        "Crystal": "",
        "Ivory": "Crystal",
        "Lace": "Ivory",
        "Silk": "Lace",
        "Steel": "Silk",
        "Tin": "Steel",
        "Pottery": "Tin",
        "Bronze": "Pottery",
        "Copper": "Bronze",
        "Sugar": "Copper",
        "Wood": "Sugar",
        "Fruit": "Wood",
        "Leather": "Fruit",
        "Cotton": "Leather",
        "Paper": "Cotton",

        }


# this will replace
def replace(column_to_replace, replace_from, replace_to):
    df[column_to_replace] = df[column_to_replace].str.replace(replace_from, replace_to)

    return df


for column in column_to_replace:
    # next loop for dictionary here
    for x, y in data.items():
        replace_from = x
        replace_to = y
        replace(column, replace_from, replace_to)

print(df['item_name'])

output = df.to_csv("test29.csv")