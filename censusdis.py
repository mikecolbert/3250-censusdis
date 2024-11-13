import censusdis.data as ced
from censusdis.datasets import ACS5
from censusdis import states

import pandas as pd


dataset = ACS5  # ACS 5-year dataset
vintage = 2022  # set to the most recent year available

# variables to download:
# 'NAME' (for the county name)
# 'B19013_001E' (for median household income)
# 'B01003_001E' (for total population)
# 'B23025_005E' (for unemployed individuals)
# 'B23025_002E' (for total civilian labor force)
variables = ["NAME", "B19013_001E", "B01003_001E", "B23025_005E", "B23025_002E"]

# geography: All counties in Iowa (state code IA)
state = states.IA
county = "*"  # data for all counties in Iowa

# pull the data
df_data = ced.download(
    dataset=dataset,
    vintage=vintage,
    download_variables=variables,
    state=state,
    county=county,
)

print(df_data)


# 'B19013_001E' (for median household income)
# 'B01003_001E' (for total population)
# 'B23025_005E' (for unemployed individuals)
# 'B23025_002E' (for total civilian labor force)

df_data = df_data.rename(
    columns={
        "B19013_001E": "median_household_income",
        "B01003_001E": "total_population",
        "B23025_005E": "unemployed_individuals",
        "B23025_002E": "total_labor_force",
    }
)

print(df_data)

# # calculate unemployment rate
# df_data["unemployment_rate_%"] = (
#     df_data["unemployed_individuals"] / df_data["total_labor_force"]
# ) * 100

# df_data["state"] = "Iowa"
# print(df_data)

# df_data["county"] = df_data["NAME"].str[:-13]
# print(df_data)

# # df_data = df_data.drop(columns=["NAME", "STATE", "COUNTY"])
# df_data = df_data[["state", "county", "total_population", "median_household_income"]]
# print(df_data)

df_data.to_csv("iowa_acs2022.csv", header=True, index=False, encoding="utf-8")
