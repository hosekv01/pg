def jaccardova_vzdalenost_mnozin(mnozina_1, mnozina_2):
    set1 = set(mnozina_1)
    set2 = set(mnozina_2)

    prunik = set1.intersection(set2)
    sjednoceni = set1.union(set2)

    jaccard_index = len(prunik) / len(sjednoceni)
    jaccard_distance = 1 - jaccard_index

    return jaccard_distance

if __name__ == "__main__":
    serp1 = ["www.seznam.cz", "www.google.com", "www.facebook.com", "www.youtube.com", "www.wikipedia.org", "www.czechia.cz"]
    serp2 = ["www.google.com", "www.facebook.com", "www.instagram.com", "www.twitter.com", "www.linkedin.com", "www.wikipedia.org"]
    serp3 = ["www.reddit.com", "www.quora.com", "www.instagram.com", "www.wikipedia.org", "www.github.com", "www.stackoverflow.com"]

    print(jaccardova_vzdalenost_mnozin(serp1, serp2))  
    print(jaccardova_vzdalenost_mnozin(serp1, serp3))  
    print(jaccardova_vzdalenost_mnozin(serp2, serp3)) 
