import numpy as np
import pandas as pd

def main():
    df = pd.read_csv('movies_5000_.csv')
    print("_"*70)
    print(df.columns)
    print(df.shape)
    print(df.head(6))

    #podstawowe statystyki
    print(f"średnia ocena: {df['rating'].mean()}")
    print(f"średni budżet: {df['budget_usd'].mean()}")

    print("_"*70)
    print("\n----NUMPY---")
    ratings = df['rating'].to_numpy()
    budgets = df['budget_usd'].to_numpy()
    revenues = df['revenue_usd'].to_numpy()

    print(f"średnia ocen: {np.mean(ratings)}")
    print(f"mediana ocen: {np.median(ratings)}")
    print(f"odchylenie standardowe: {np.std(ratings)}")

    print("_" * 70)
    print(f"ROI(Return on Investment) = {revenues / budgets}")
    roi = np.divide(revenues, budgets,out=np.zeros_like(revenues,dtype=float), where=budgets>0)
    df["ROI"] = roi
    #top10 filmów wg ROI
    top10 = df.sort_values(by='ROI',ascending=False)[:10]
    print("_" * 70)
    print(top10[['title','year','revenue_usd','budget_usd','ROI']].head(10))

    #grupowanie
    genre_groups = df.groupby('genre')['rating'].apply(lambda x: np.mean(x.to_numpy()))
    print("_"*70)
    print(genre_groups)


if __name__ == '__main__':
    main()
