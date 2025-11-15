#MapPlot.py
#Name: Grant Schaeffer
#Date: 11/14/2025
#Assignment: Lab 10

import election
import pandas
import matplotlib.pyplot as plt
result = election.get_result()

locates = []
votes = []

for place in result:
    locate = place["Location"]["County"]
    vote = place["Vote Data"]["Ben Carson"]["Number of Votes"]
    locates.append(locate)
    votes.append(vote)
    print(locate, vote)

df = pandas.DataFrame([{"Locate": locates,
                        "Vote": votes}])

print(df)

#df.plot(kind = "scatter", x = "Locate", y = "Vote")
plt.plot(locates, votes, "ro")
plt.savefig("output")
#The datasetchosen describes results from the 2016 election.
#Ben Carson is the subject of this graph.
#The graph represents the amounts of votes he recieved.
#The graph displays votes in terms of county of where the vote was placed.