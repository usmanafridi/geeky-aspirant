import spacy
#loading the english language small model of spacy
en = spacy.load('en_core_web_sm')
stopwords = en.Defaults.stop_words

text = """ Nizar Hassan was born in 1960 and raised in the village of Mashhad, near Nazareth, where he has lived with his
family. He studied anthropology at Haifa University and after graduating worked in TV. Starting in 1990, he
turned to cinema. In 1994, he produced Independence, in which he pokes his Palestinian interlocutors about what
they think of the bizarre Israeli notion of their “independence”. They have stolen another people’s homeland and
call the act “independence”! Hassan dwells on that absurdity.
As the world’s attention was captured by the news of Israel planning to “annex” yet a bit more of Palestine and
add it to what they have already stolen, I received an email from Nizar Hassan, the pre-eminent Palestinian
documentary filmmaker. He wrote to me about his latest film, My Grandfather’s Path, and included a link to the
director’s cut. It was a blessing. They say choose your enemies carefully for you would end up like them. The
same goes for those opposing Zionist settler colonialists. If you are too incensed and angered by their daily dose of
claptrap, the vulgarity of their armed robbery of Palestine, you would soon become like them and forget yourself
and what beautiful ideas, ideals, and aspirations once animated your highest dreams. Never fall into that trap. For
decades, aspects of Palestinian and world cinema, art, poetry, fiction, and drama have done for me precisely that:
saved me from that trap. They have constantly reminded me what all our politics are about – a moment of poetic
salvation from it all.
Nizar Hassan’s new documentary is one such work – in a moment of dejection over Israel’s encroachment on
Palestinian rights and the world’s complicity, it has put Palestine in perspective. The film is mercifully long,
beautifully paced and patient, a masterfully crafted work of art – a Palestinian’s epic ode to his homeland. A
shorter version of My Grandfather’s Path has been broadcast on Al Jazeera Arabic in three parts, but it must be
seen in its entirety, in one go. It is a pilgrimage that must not be interrupted. """
lst=[]
for token in text.split():
    if token.lower() not in stopwords:    #checking whether the word is not 
        lst.append(token)                    #present in the stopword list.
        
#Join items in the list
print("Original text  : ",text)
print("Text after removing stopwords  :   ",' '.join(lst))

new_list= ' '.join(lst)
# print(new_list)
print(len(text))
print(len(new_list))
# 1. Marine
# 2. Intrigue
# 3. North-South
# 4. Topography
# 5. Peninsula
# 6. Latitude
# 7. Meridian


# ## After using Stopwords in 
# 1. 
# Marine
# 2. 
# Intrigue
# 3. 
# North-South
# 4. 
# Topography
# 5. 
# Peninsula
# 6. 
# Latitude
# 7. 
# Meridian


# # 2ns passage answers 
# # Original

# 8. Amicable 

# 9. Blithe 

# 10. Disgruntled 

# 11. Defiantly 

# 12. Despondently 

# 13. Desolation 

# 14. Disillusioned

#after stopwords:

# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Answer the questions from the following passage :\nMarie Curie accomplished scientists history. husband, Pierre, discovered radium, element widely treating cancer, studied uranium radioactive substances. Pierre Marie’s amicable collaboration later helped unlock secrets atom. Marie born 1867 Warsaw, Poland, father professor physics. early age, displayed brilliant mind blithe personality. great exuberance learning prompted continue studies high school. disgruntled, however, learned university Warsaw closed women. Determined receive higher education, defiantly left Poland 1891 entered Sorbonne, French university, earned master’s degree doctorate physics. Marie fortunate studied Sorbonne greatest scientists day, Pierre Curie. Marie Pierre married 1895 spent productive years working physics laboratory. short time discovered radium, Pierre killed horse-drawn wagon 1906. Marie stunned horrible misfortune endured heartbreaking anguish. Despondently recalled close relationship joy shared scientific research. fact young daughters raise greatly increased distress. Curie’s feeling desolation finally began fade asked succeed husband physics professor Sorbonne. woman given professorship world-famous university. 1911 received Nobel Prize chemistry isolating radium. Marie Curie eventually suffered fatal illness long exposure radium, disillusioned work. Regardless consequences, dedicated science revealing mysteries physical world.\nQuestions:\n\nWhy was Marie disgruntled?\n\nMarie was disgruntled because she learned that the university in Warsaw was closed to women.",
#   temperature=0.7,
#   max_tokens=24,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )