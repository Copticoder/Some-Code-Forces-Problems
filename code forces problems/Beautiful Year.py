year=int(input())
year+=1
# yearInt=year
year=str(year)

while (
    year[0] in [year[1], year[2], year[3]]
    or year[1] in [year[2], year[3]]
    or year[2] == year[3]
):
    year=int(year)
    year+=1
    year=str(year)
print(year)