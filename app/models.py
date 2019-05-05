# models.py : Data Generator for Displaying on Web pages

def cp_sites():
    class CP_Sites:
        def __init__(self, img, url):
            self.img = img
            self.url = url

    sites = []
    sites.append (CP_Sites ("codeforces.png", "https://codeforces.com"))
    sites.append (CP_Sites ("atcoder.png", "https://atcoder.jp"))
    sites.append (CP_Sites ("codechef.jpg", "https://www.codechef.com"))
    sites.append (CP_Sites ("hackerearth.png", "https://www.hackerearth.com"))
    sites.append (CP_Sites ("spoj.png", "https://www.spoj.com"))
    sites.append (CP_Sites ("uva.png", "https://uva.onlinejudge.org"))
    sites.append (CP_Sites ("hackerrank.svg", "https://www.hackerrank.com"))
    sites.append (CP_Sites ("project_euler.png", "https://projecteuler.net"))
    sites.append (CP_Sites ("codejam.jpg", 
            "https://codingcompetitions.withgoogle.com/codejam/archive"))
    sites.append (CP_Sites ("icpc.png", 
        "https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8"))
    return sites
