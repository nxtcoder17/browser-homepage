# models.py : Data Generator for Displaying on Web pages

def cp_sites():
    class CP_Sites:
        def __init__(self, img, url):
            self.img = "cp/" + img
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

def study_sites():
    class StudySites:
        def __init__ (self, img, url):
            self.img = "study/" + img;
            self.url = url

    sites = []
    sites.append (StudySites ("safari.png", "https://learning.oreilly.com"))
    sites.append (StudySites ("cppreference.png", "https://en.cppreference.com"))
    sites.append (StudySites ("real_python.jpg", "https://realpython.com"))
    sites.append (StudySites ("cognitive_class.png", "https://cognitiveclass.ai"))
    sites.append (StudySites ("coding_alpha.png", "https://www.codingalpha.com/"))
    return sites

def football_sites():
    class Container:
        def __init__ (self, img, url):
            self.img = 'football/' + img;
            self.url = url

    sites = []
    sites.append (Container ("goal.jpg", "https://www.goal.com"))
