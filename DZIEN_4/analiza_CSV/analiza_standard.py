import csv

def read_movie(path: str):
    movies = []
    with open(path,'r',newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['year'] = int(row['year'])
            row['rating'] = float(row['rating'])
            row['budget_usd'] = float(row['budget_usd'])
            movies.append(row)
    return movies

def main():
    movies = read_movie('movies_5000_.csv')

    #pierwsze 5 filmów
    print("pierwsze 5 filmów")
    for m in movies[:5]:
        print(m['title'],m['year'],m['genre'],m['rating'])

    #filmy po roku 2015
    after_2015 = [m for m in movies if m['year'] >= 2015]
    print(f"\nliczba filmów po roku 2015: {len(after_2015)}")

    #top10 filmów pod kątem ratingu
    top10 = sorted(movies,key=lambda m:m['rating'],reverse=True)[:10]
    print("_"*70)
    print("top 10 - filmy z najwyższą oceną")
    for m in top10:
        print(m['title'],m['year'],m['rating'])

    #filmy z Polski
    poland = [m for m in movies if m['country'] == 'Poland']
    print("_" * 70)
    print(f"liczba filmów z Polski: {len(poland)}")

    #średnia ocen
    avg_rating = sum(m["rating"] for m in movies) / len(movies)
    print("_" * 70)
    print(f"średnia ocena: {avg_rating}")

    #film z majwyższym budżetem
    max_budget = max(movies,key=lambda m: m['budget_usd'])
    print("_" * 70)
    print(f"film z najwięszym budżetem: {max_budget['title']}, {max_budget['budget_usd']}")



if __name__ == '__main__':
    main()
