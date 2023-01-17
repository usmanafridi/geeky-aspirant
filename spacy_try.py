import spacy
#loading the english language small model of spacy
en = spacy.load('en_core_web_sm')
stopwords = en.Defaults.stop_words

text = """ Globalization is viewed by its proponents as a process of cementing economic, cultural and political bonds between peoples of
different countries of the world. One may regard it as a process by which they are welded into a single world society, to be termed
as global society. It means internationalization of production and labour leading to integration of economies of developing and
developed countries into global economy. To quote Rosaberth M.Kanter, “The world is becoming a global shopping mall in which
ideas and products are available everywhere at the same time.”
Globalization is a natural outcome of computer networking and electronic mass communication. Information technology has made
it possible for nations of the world to contact one another beyond their national borders. Besides, globalization is also promoted
through the growth and proliferation of multinational companies and corporations that operate as transporter networks. Anyhow the
flow of capital technology and labour across the borders of countries has accentuated the process of globalization.
Deregulation, liberalism and privatization being assiduously pursued in the developing countries are some other manifestations of
globalization. These countries are opening their economies to follow these trends. The size of the public sector is shrinking for the
private sector to assume an increasingly important role in the economic development of the Third World countries. The downsizing
of the public sector is in line with the spirit of market economy. This is suggested as a measure to cover up their fiscal deficit.."""
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