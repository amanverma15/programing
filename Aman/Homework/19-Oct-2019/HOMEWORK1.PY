print("1.")
a = "Artificail"
print(len(a))
print("----------------------------------------------------------------------------------------")
print("2.")
def chf(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(chf("""In the novel  Percy Jackson And The Olympians, Percy, Annabeth, Tyson are in the main character of the Novel. When I read the book I view Percy as a normal kid but has a secret other life. Tyson(Percy’s friend) view him as a nice person because of him being his friend before Tyson did not have any friends. Right now I am on pg 112 out of 224. At the beginning of the story in an innocent game of dodgeball among Percy and his classmates turns into a death match against an ugly gang of cannibal giants. Soon an unexpected arrival of Percy’s friend Annabeth brings more bad news: The magical border that protects Camp Half-Blood has been poisoned. From then on Percy goes camping half-blood with an unexpected event of bulls entering Camp Half-Blood to flames coming out of the bull's mouth. Then suddenly Percy became a target of both the bulls. Then suddenly Tyson protected Percy by blocking the 1000 degree flames. After Tyson punched the bull and broke its skeleton. After the big fight, Percy and Annabeth have been trying to figure out who Poisoned the border and where to find the cure. Soon they got an idea that the person or monster may have come from the Sea of Monster to infiltrate Camp Half-Blood border. (The Border is a magical tree that has come from the sacrifice of Thalia)(that's where I left off). According to the story, I read so far I believe Percy and Annabeth are going to the Sea of Monster because it might be the place where they might find the cure to the Tree that protects Camp Half-Blood. This evidence proves the point because, without the border, Camp Half-Blood will be destroyed from the Monster in the  Sea of Monsters. """))
print("----------------------------------------------------------------------------------------")
print("3.")
